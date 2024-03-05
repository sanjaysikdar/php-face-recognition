import face_recognition, sys
from urllib.parse import urlparse
import urllib.request



def is_url(path):
    """Check if the path is a URL."""
    # return path.startswith(('http://', 'https://', 'ftp://'))
    return urlparse(path).scheme != ''


def authenticate_user(known_image_path, unknown_image_path):
    try:
        if is_url(known_image_path):
            known_image_path = urllib.request.urlopen(known_image_path)
            
        if is_url(unknown_image_path):
            unknown_image_path = urllib.request.urlopen(unknown_image_path)
            
        # Load known image and encode faces
        known_image = face_recognition.load_image_file(known_image_path)
        known_encoding = face_recognition.face_encodings(known_image)[0]

        # Load unknown image and encode faces
        unknown_image = face_recognition.load_image_file(unknown_image_path)
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

        # Compare faces
        results = face_recognition.compare_faces([known_encoding], unknown_encoding, tolerance=0.5)
        # Compare faces and get distance
        distance = face_recognition.face_distance([known_encoding], unknown_encoding)

        # Convert distance to confidence score (1 - distance)
        confidence_score = 1 - distance[0]
        return (results[0], confidence_score) if results[0] else (results[0], 0)

    except Exception as e:
        return str(e)



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python face_r.py <known_image_path> <unknown_image_path>")
        sys.exit(1)

    known_image_path = sys.argv[1]
    unknown_image_path = sys.argv[2]

    result = authenticate_user(known_image_path, unknown_image_path)
    print(result)
   