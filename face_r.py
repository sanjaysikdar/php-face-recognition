import face_recognition
import sys

def authenticate_user(known_image_path, unknown_image_path):
    try:
        # Load known image and encode faces
        known_image = face_recognition.load_image_file(known_image_path)
        known_encoding = face_recognition.face_encodings(known_image)[0]

        # Load unknown image and encode faces
        unknown_image = face_recognition.load_image_file(unknown_image_path)
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

        # Compare faces
        results = face_recognition.compare_faces([known_encoding], unknown_encoding, tolerance=0.5)

        return results[0]
    except Exception as e:
        return str(e)



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python face_authentication.py <known_image_path> <unknown_image_path>")
        sys.exit(1)

    known_image_path = sys.argv[1]
    unknown_image_path = sys.argv[2]

    result = authenticate_user(known_image_path, unknown_image_path)

    if result:
        print("Authentication successful!")
    else:
        print("Authentication failed.")