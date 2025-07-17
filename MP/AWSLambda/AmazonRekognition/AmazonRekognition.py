import json
import boto3
import base64

rekognition = boto3.client('rekognition')


def validate_required_params(event, required_keys):
    missing = [k for k in required_keys if not event.get(k)]
    if missing:
        raise ValueError(f"Missing required parameter(s): {', '.join(missing)}")


def decode_image_param(event, key):
    try:
        if key in event and event[key]:
            return base64.b64decode(event[key])
    except Exception:
        raise ValueError(f"Invalid base64 encoding for '{key}'")
    return None


def lambda_handler(event, context):
    try:
        operation = event.get('operation')
        if not operation:
            return {"statusCode": 400, "body": json.dumps({"error": "Missing required parameter: operation"})}
        
        operation = operation.upper()
        response = {}

        
        if operation == "DETECTTEXT":
            image_bytes = decode_image_param(event, 'imageFormat')
            validate_required_params(event, ['imageFormat'])
            response = rekognition.detect_text(Image={"Bytes": image_bytes})

        elif operation == "DETECTLABELS":
            image_bytes = decode_image_param(event, 'imageFormat')
            validate_required_params(event, ['imageFormat'])
            params = {"Image": {"Bytes": image_bytes}}
            if "MaxLabels" in event:
                params["MaxLabels"] = int(event["MaxLabels"])
            if "MinConfidence" in event:
                params["MinConfidence"] = float(event["MinConfidence"])
            response = rekognition.detect_labels(**params)

        elif operation == "DETECTMODERATIONLABELS":
            image_bytes = decode_image_param(event, 'imageFormat')
            validate_required_params(event, ['imageFormat'])
            params = {"Image": {"Bytes": image_bytes}}
            if "MinConfidence" in event:
                params["MinConfidence"] = float(event["MinConfidence"])
            response = rekognition.detect_moderation_labels(**params)

        elif operation == "DETECTFACES":
            image_bytes = decode_image_param(event, 'imageFormat')
            validate_required_params(event, ['imageFormat'])
            response = rekognition.detect_faces(Image={"Bytes": image_bytes})

        elif operation == "COMPAREFACES":
            source_image = decode_image_param(event, 'sourceImageFormat')
            target_image = decode_image_param(event, 'imageFormat')
            validate_required_params(event, ['sourceImageFormat', 'imageFormat'])
            params = {
                "SourceImage": {"Bytes": source_image},
                "TargetImage": {"Bytes": target_image}
            }
            if "SimilarityThreshold" in event:
                params["SimilarityThreshold"] = float(event["SimilarityThreshold"])
            response = rekognition.compare_faces(**params)

        elif operation == "INDEXFACES":
            image_bytes = decode_image_param(event, 'imageFormat')
            validate_required_params(event, ['imageFormat', 'collectionId'])
            response = rekognition.index_faces(
                CollectionId=event["collectionId"],
                Image={"Bytes": image_bytes}
            )

        elif operation == "SEARCHFACESBYIMAGE":
            image_bytes = decode_image_param(event, 'imageFormat')
            validate_required_params(event, ['imageFormat', 'collectionId'])
            response = rekognition.search_faces_by_image(
                CollectionId=event["collectionId"],
                Image={"Bytes": image_bytes}
            )

        elif operation == "SEARCHFACES":
            validate_required_params(event, ['collectionId', 'FaceId'])
            response = rekognition.search_faces(
                CollectionId=event["collectionId"],
                FaceId=event["FaceId"]
            )

        elif operation == "LISTFACES":
            validate_required_params(event, ['collectionId'])
            response = rekognition.list_faces(CollectionId=event["collectionId"])

        elif operation == "DELETEFACES":
            validate_required_params(event, ['collectionId', 'FaceIds'])
            response = rekognition.delete_faces(
                CollectionId=event["collectionId"],
                FaceIds=event["FaceIds"]
            )

        elif operation == "CREATECOLLECTION":
            validate_required_params(event, ['collectionId'])
            response = rekognition.create_collection(CollectionId=event["collectionId"])

        elif operation == "DELETECOLLECTION":
            validate_required_params(event, ['collectionId'])
            response = rekognition.delete_collection(CollectionId=event["collectionId"])

        elif operation == "LISTCOLLECTIONS":
            response = rekognition.list_collections()

        elif operation == "RECOGNIZECELEBRITIES":
            image_bytes = decode_image_param(event, 'imageFormat')
            validate_required_params(event, ['imageFormat'])
            response = rekognition.recognize_celebrities(Image={"Bytes": image_bytes})

        elif operation == "DETECTPROTECTIVEEQUIPMENT":
            image_bytes = decode_image_param(event, 'imageFormat')
            validate_required_params(event, ['imageFormat'])
            response = rekognition.detect_protective_equipment(Image={"Bytes": image_bytes})

        else:
            return {"statusCode": 400, "body": json.dumps({"error": f"Unsupported operation: {operation}"})}

        return {"statusCode": 200, "body": json.dumps(response, default=str)}

    except ValueError as ve:
        return {"statusCode": 400, "body": json.dumps({"error": str(ve)})}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
