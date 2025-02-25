import requests
import json
from pathlib import Path

def test_photo_verification(image_paths=['IMG_1347.jpeg', 'IMG_1348.jpeg']):
    # API endpoint URL
    url = "http://localhost:8000/classify-photos/"
    
    try:
        # Open files and create MultipartEncoder
        files = []
        for img_path in image_paths:
            # Check if file exists
            if not Path(img_path).exists():
                raise FileNotFoundError(f"Image file not found: {img_path}")
                
            # Open file and add to files list
            files.append(
                ('photos', (
                    Path(img_path).name,
                    open(img_path, 'rb'),
                    'image/jpeg'  # Adjust content type if needed
                ))
            )

        # Add the task parameter
        data = {
            'task': 'Reduce electricity consumption'
        }

        # Make request with debug information
        print(f"Making request to {url}")
        print("Files being sent:", [f[1][0] for f in files])
        print("Data being sent:", data)
        
        response = requests.post(url, files=files, params=data)
        
        # Print detailed response information
        print("\nResponse Status Code:", response.status_code)
        print("Response Headers:", dict(response.headers))
        
        try:
            print("Response Content:", response.json())
        except json.JSONDecodeError:
            print("Raw Response Content:", response.text)
            
        if response.status_code == 422:
            print("\nValidation Error Details:")
            error_detail = response.json().get('detail', [])
            for error in error_detail:
                print(f"- Location: {error.get('loc', '')}")
                print(f"  Message: {error.get('msg', '')}")
                print(f"  Type: {error.get('type', '')}")

        return response

    except Exception as e:
        print(f"Error: {str(e)}")
        return None
    
    finally:
        # Close all file handles
        for _, (_, file_obj, _) in files:
            file_obj.close()

if __name__ == "__main__":
    # Test with specific image paths
    result = test_photo_verification()
    
    if result and result.status_code == 200:
        print("\nTest completed successfully!")
    else:
        print("\nTest failed!")
