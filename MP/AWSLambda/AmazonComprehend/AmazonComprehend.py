import boto3
import json
import datetime

def json_serial(obj):
    """JSON serializer for objects not serializable by default"""
    if isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

def lambda_handler(event, context):
    comprehend = boto3.client('comprehend')
    operation = event.get("operation")

    
    if operation == "DetectDominantLanguage":
        response = comprehend.detect_dominant_language(Text=event.get("Text", ""))
        return response

    elif operation == "DetectEntities":
        response = comprehend.detect_entities(
            Text=event.get("Text", ""),
            LanguageCode=event.get("LanguageCode", "en")
        )
        return response

    elif operation == "DetectKeyPhrases":
        response = comprehend.detect_key_phrases(
            Text=event.get("Text", ""),
            LanguageCode=event.get("LanguageCode", "en")
        )
        return response

    elif operation == "DetectPiiEntities":
        response = comprehend.detect_pii_entities(
            Text=event.get("Text", ""),
            LanguageCode=event.get("LanguageCode", "en")
        )
        return response

    elif operation == "DetectSentiment":
        response = comprehend.detect_sentiment(
            Text=event.get("Text", ""),
            LanguageCode=event.get("LanguageCode", "en")
        )
        return response

    elif operation == "DetectSyntax":
        response = comprehend.detect_syntax(
            Text=event.get("Text", ""),
            LanguageCode=event.get("LanguageCode", "en")
        )
        return response

    elif operation == "DetectTargetedSentiment":
        response = comprehend.detect_targeted_sentiment(
            Text=event.get("Text", ""),
            LanguageCode=event.get("LanguageCode", "en")
        )
        return response

    elif operation == "DetectToxicContent":
        response = comprehend.detect_toxic_content(
            TextSegments=event.get("TextSegments", []),
            LanguageCode=event.get("LanguageCode", "en")
        )
        return response

    elif operation == "ContainsPiiEntities":
        response = comprehend.contains_pii_entities(
            Text=event.get("Text", ""),
            LanguageCode=event.get("LanguageCode", "en")
        )
        return response
    
    elif operation == "BatchDetectDominantLanguage":
        response = comprehend.batch_detect_dominant_language(TextList=event.get("TextList", []))
        return response

    elif operation == "BatchDetectEntities":
        response = comprehend.batch_detect_entities(
            TextList=event.get("TextList", []),
            LanguageCode=event.get("LanguageCode", "en")
        )
        return response

    elif operation == "BatchDetectKeyPhrases":
        response = comprehend.batch_detect_key_phrases(
            TextList=event.get("TextList", []),
            LanguageCode=event.get("LanguageCode", "en")
        )
        return response

    elif operation == "BatchDetectSentiment":
        response = comprehend.batch_detect_sentiment(
            TextList=event.get("TextList", []),
            LanguageCode=event.get("LanguageCode", "en")
        )
        return response

    elif operation == "BatchDetectSyntax":
        response = comprehend.batch_detect_syntax(
            TextList=event.get("TextList", []),
            LanguageCode=event.get("LanguageCode", "en")
        )
        return response

    elif operation == "BatchDetectTargetedSentiment":
        response = comprehend.batch_detect_targeted_sentiment(
            TextList=event.get("TextList", []),
            LanguageCode=event.get("LanguageCode", "en")
        )
        return response

    elif operation == "TagResource":
        response = comprehend.tag_resource(
            ResourceArn=event.get("ResourceArn", ""),
            Tags=event.get("Tags", [])
        )
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Tags added successfully"})
        }

    elif operation == "UntagResource":
        response = comprehend.untag_resource(
            ResourceArn=event.get("ResourceArn", ""),
            TagKeys=event.get("TagKeys", [])
        )
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Tags removed successfully"})
        }

    elif operation == "ClassifyDocument":
        classify_params = {
            "EndpointArn": event.get("EndpointArn", ""),
        }
        if "Text" in event:
            classify_params["Text"] = event["Text"]
        if "Bytes" in event:
            classify_params["Bytes"] = event["Bytes"]
        if "DocumentReaderConfig" in event:
            classify_params["DocumentReaderConfig"] = event["DocumentReaderConfig"]

        response = comprehend.classify_document(**classify_params)
        return response

    elif operation == "DeleteDocumentClassifier":
        response = comprehend.delete_document_classifier(
            DocumentClassifierArn=event.get("DocumentClassifierArn", "")
        )
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Document classifier deleted successfully"})
        }

    elif operation == "StartDocumentClassificationJob":
        response = comprehend.start_document_classification_job(
            ClientRequestToken=event.get("ClientRequestToken", ""),
            DataAccessRoleArn=event.get("DataAccessRoleArn", ""),
            DocumentClassifierArn=event.get("DocumentClassifierArn", ""),
            FlywheelArn=event.get("FlywheelArn", ""),
            InputDataConfig=event.get("InputDataConfig", {}),
            JobName=event.get("JobName", ""),
            OutputDataConfig=event.get("OutputDataConfig", {}),
            Tags=event.get("Tags", []),
            VolumeKmsKeyId=event.get("VolumeKmsKeyId", ""),
            VpcConfig=event.get("VpcConfig", {})
        )
        return response

    elif operation == "ListDocumentClassificationJobs":
        response = comprehend.list_document_classification_jobs(
            Filter=event.get("Filter", {}),
            MaxResults=event.get("MaxResults", 10),
            NextToken=event.get("NextToken", "")
        )
        return response

    elif operation == "DescribeDocumentClassificationJob":
        response = comprehend.describe_document_classification_job(
            JobId=event.get("JobId", "")
        )
        return response

    elif operation == "DescribeDocumentClassifier":
        response = comprehend.describe_document_classifier(
            DocumentClassifierArn=event.get("DocumentClassifierArn", "")
        )
        return response 
    elif operation == "DescribeDominantLanguageDetectionJob":
        response = comprehend.describe_dominant_language_detection_job(
            JobId=event.get("JobId", "")
        )
        return json.loads(json.dumps(response, default=json_serial))


    elif operation == "DescribeEntitiesDetectionJob":
        response = comprehend.describe_entities_detection_job(
            JobId=event.get("JobId", "")
        )
        return json.loads(json.dumps(response, default=json_serial))
    
    elif operation == "DescribeEntityRecognizer":
        response = comprehend.describe_entity_recognizer(
            EntityRecognizerArn=event.get("EntityRecognizerArn", "")
        )
        return response

    elif operation == "DescribeEventsDetectionJobcribe":
        response = comprehend.describe_events_detection_job(
            JobId=event.get("JobId", "")
        )
        return json.loads(json.dumps(response, default=json_serial))
    elif operation == "DescribeFlywheel":
        response = comprehend.describe_flywheel(
            FlywheelArn=event.get("FlywheelArn", "")
        )
        return response
    elif operation == "DescribeKeyPhrasesDetectionJob":
        response = comprehend.describe_key_phrases_detection_job(
            JobId=event.get("JobId", "")
        )
        return json.loads(json.dumps(response, default=json_serial))
    elif operation == "DescribePiiEntitiesDetectionJob":
        response = comprehend.describe_pii_entities_detection_job(
            JobId=event.get("JobId", "")
        )
        return json.loads(json.dumps(response, default=json_serial))
    elif operation == "DescribeResourcePolicy":
        response = comprehend.describe_resource_policy(
            ResourceArn=event.get("ResourceArn", "")
        )
        return response
    elif operation == "DescribeTargetedSentimentDetectionJob":
        response = comprehend.describe_targeted_sentiment_detection_job(
            JobId=event.get("JobId", "")
        )
        return json.loads(json.dumps(response, default=json_serial))
    elif operation == "DescribeSentimentDetectionJob":
        response = comprehend.describe_sentiment_detection_job(
            JobId=event.get("JobId", "")
        )
        return json.loads(json.dumps(response, default=json_serial))

    elif operation == "DescribeTopicsDetectionJob":
        response = comprehend.describe_topics_detection_job(
            JobId=event.get("JobId", "")
        )
        return json.loads(json.dumps(response, default=json_serial))

    
    elif operation == "StartDominantLanguageDetectionJob":
    
        # Validate and construct InputDataConfig
        input_config = event.get("InputDataConfig", {})
        if "S3Uri" not in input_config or not input_config["S3Uri"]:
            return {"Error": "InputDataConfig.S3Uri is required"}

        input_data_config = {
            "S3Uri": input_config["S3Uri"]
        }

        if "InputFormat" in input_config and input_config["InputFormat"]:
            input_data_config["InputFormat"] = input_config["InputFormat"]

        if "DocumentReaderConfig" in input_config and input_config["DocumentReaderConfig"]:
            drc = input_config["DocumentReaderConfig"]
            doc_reader_config = {}

            if "DocumentReadAction" in drc and drc["DocumentReadAction"]:
                doc_reader_config["DocumentReadAction"] = drc["DocumentReadAction"]

            if "DocumentReadMode" in drc and drc["DocumentReadMode"]:
                doc_reader_config["DocumentReadMode"] = drc["DocumentReadMode"]

            if "FeatureTypes" in drc:
                feature_types = [ft for ft in drc["FeatureTypes"] if isinstance(ft, str) and ft.strip()]
                if feature_types:
                    doc_reader_config["FeatureTypes"] = feature_types

            if doc_reader_config:
                input_data_config["DocumentReaderConfig"] = doc_reader_config

        # Validate and construct OutputDataConfig
        output_config = event.get("OutputDataConfig", {})
        if "S3Uri" not in output_config or not output_config["S3Uri"]:
            return {"Error": "OutputDataConfig.S3Uri is required"}

        output_data_config = {
            "S3Uri": output_config["S3Uri"]
        }

        if "KmsKeyId" in output_config and output_config["KmsKeyId"]:
            output_data_config["KmsKeyId"] = output_config["KmsKeyId"]

        # Build kwargs for API call
        kwargs = {
            "InputDataConfig": input_data_config,
            "OutputDataConfig": output_data_config,
            "DataAccessRoleArn": event.get("DataAccessRoleArn")
        }

        if "JobName" in event and event["JobName"]:
            kwargs["JobName"] = event["JobName"]

        if "ClientRequestToken" in event and isinstance(event["ClientRequestToken"], str) and event["ClientRequestToken"].strip():
            kwargs["ClientRequestToken"] = event["ClientRequestToken"]

        if "Tags" in event and isinstance(event["Tags"], list):
            valid_tags = [
                tag for tag in event["Tags"]
                if tag.get("Key") and tag.get("Value")
            ]
            if valid_tags:
                kwargs["Tags"] = valid_tags

        if "VolumeKmsKeyId" in event and event["VolumeKmsKeyId"]:
            kwargs["VolumeKmsKeyId"] = event["VolumeKmsKeyId"]

        if "VpcConfig" in event and event["VpcConfig"]:
            kwargs["VpcConfig"] = event["VpcConfig"]

        # Call Comprehend
        response = comprehend.start_dominant_language_detection_job(**kwargs)
        return response

    elif operation == "ListDominantLanguageDetectionJobs":
    
        kwargs = {}

        # Handle Filter block
        filter_block = event.get("Filter")
        if filter_block:
            filter_obj = {}

            if "JobName" in filter_block and filter_block["JobName"]:
                filter_obj["JobName"] = filter_block["JobName"]

            if "JobStatus" in filter_block and filter_block["JobStatus"]:
                filter_obj["JobStatus"] = filter_block["JobStatus"]

            if "SubmitTimeAfter" in filter_block and isinstance(filter_block["SubmitTimeAfter"], (int, float)):
                filter_obj["SubmitTimeAfter"] = filter_block["SubmitTimeAfter"]

            if "SubmitTimeBefore" in filter_block and isinstance(filter_block["SubmitTimeBefore"], (int, float)):
                filter_obj["SubmitTimeBefore"] = filter_block["SubmitTimeBefore"]

            if filter_obj:
                kwargs["Filter"] = filter_obj

        # Optional MaxResults
        if "MaxResults" in event and isinstance(event["MaxResults"], int):
            kwargs["MaxResults"] = event["MaxResults"]

        # Optional NextToken
        if "NextToken" in event and isinstance(event["NextToken"], str) and event["NextToken"].strip():
            kwargs["NextToken"] = event["NextToken"]

        # Call the Comprehend API
        response = comprehend.list_dominant_language_detection_jobs(**kwargs)
        return json.loads(json.dumps(response, default=json_serial))


    
    elif operation == "StopDominantLanguageDetectionJob":
        response = comprehend.stop_dominant_language_detection_job(
            JobId=event.get("JobId", "")
        )
        return response
    
    elif operation == "StartEntitiesDetectionJob":
        # Validate required InputDataConfig.S3Uri
        input_config = event.get("InputDataConfig", {})
        if "S3Uri" not in input_config or not input_config["S3Uri"]:
            return {"Error": "InputDataConfig.S3Uri is required"}

        input_data_config = {
            "S3Uri": input_config["S3Uri"]
        }

        if "InputFormat" in input_config and input_config["InputFormat"]:
            input_data_config["InputFormat"] = input_config["InputFormat"]

        if "DocumentReaderConfig" in input_config and input_config["DocumentReaderConfig"]:
            drc = input_config["DocumentReaderConfig"]
            doc_reader_config = {}

            if "DocumentReadAction" in drc and drc["DocumentReadAction"]:
                doc_reader_config["DocumentReadAction"] = drc["DocumentReadAction"]

            if "DocumentReadMode" in drc and drc["DocumentReadMode"]:
                doc_reader_config["DocumentReadMode"] = drc["DocumentReadMode"]

            if "FeatureTypes" in drc:
                feature_types = [ft for ft in drc["FeatureTypes"] if isinstance(ft, str) and ft.strip()]
                if feature_types:
                    doc_reader_config["FeatureTypes"] = feature_types

            if doc_reader_config:
                input_data_config["DocumentReaderConfig"] = doc_reader_config

        # Validate required OutputDataConfig.S3Uri
        output_config = event.get("OutputDataConfig", {})
        if "S3Uri" not in output_config or not output_config["S3Uri"]:
            return {"Error": "OutputDataConfig.S3Uri is required"}

        output_data_config = {
            "S3Uri": output_config["S3Uri"]
        }

        if "KmsKeyId" in output_config and output_config["KmsKeyId"]:
            output_data_config["KmsKeyId"] = output_config["KmsKeyId"]

        # Start building request kwargs
        kwargs = {
            "InputDataConfig": input_data_config,
            "OutputDataConfig": output_data_config,
            "DataAccessRoleArn": event.get("DataAccessRoleArn"),
            "LanguageCode": event.get("LanguageCode")
        }

        # Optional fields
        if "ClientRequestToken" in event and isinstance(event["ClientRequestToken"], str) and event["ClientRequestToken"].strip():
            kwargs["ClientRequestToken"] = event["ClientRequestToken"]

        if "EntityRecognizerArn" in event and event["EntityRecognizerArn"]:
            kwargs["EntityRecognizerArn"] = event["EntityRecognizerArn"]

        if "FlywheelArn" in event and event["FlywheelArn"]:
            kwargs["FlywheelArn"] = event["FlywheelArn"]

        if "JobName" in event and event["JobName"]:
            kwargs["JobName"] = event["JobName"]

        if "Tags" in event and isinstance(event["Tags"], list):
            valid_tags = [tag for tag in event["Tags"] if tag.get("Key") and tag.get("Value")]
            if valid_tags:
                kwargs["Tags"] = valid_tags

        if "VolumeKmsKeyId" in event and event["VolumeKmsKeyId"]:
            kwargs["VolumeKmsKeyId"] = event["VolumeKmsKeyId"]

        if "VpcConfig" in event and event["VpcConfig"]:
            vpc_config = {}
            if "SecurityGroupIds" in event["VpcConfig"]:
                vpc_config["SecurityGroupIds"] = [sg for sg in event["VpcConfig"]["SecurityGroupIds"] if sg]
            if "Subnets" in event["VpcConfig"]:
                vpc_config["Subnets"] = [sn for sn in event["VpcConfig"]["Subnets"] if sn]
            if vpc_config:
                kwargs["VpcConfig"] = vpc_config

        # Call Comprehend API
        response = comprehend.start_entities_detection_job(**kwargs)

        # Serialize datetime if necessary
        return json.loads(json.dumps(response, default=json_serial))

    
    elif operation == "StopEntitiesDetectionJob":
        response = comprehend.stop_entities_detection_job(
            JobId=event.get("JobId", "")
        )
        return response
    
    elif operation == "ListEntitiesDetectionJobs":
        kwargs = {}

        # Handle optional filter
        filter_params = event.get("Filter", {})
        filter_obj = {}

        if "JobName" in filter_params and filter_params["JobName"]:
            filter_obj["JobName"] = filter_params["JobName"]

        if "JobStatus" in filter_params and filter_params["JobStatus"]:
            filter_obj["JobStatus"] = filter_params["JobStatus"]

        if "SubmitTimeAfter" in filter_params and filter_params["SubmitTimeAfter"]:
            filter_obj["SubmitTimeAfter"] = datetime.datetime.fromtimestamp(filter_params["SubmitTimeAfter"])

        if "SubmitTimeBefore" in filter_params and filter_params["SubmitTimeBefore"]:
            filter_obj["SubmitTimeBefore"] = datetime.datetime.fromtimestamp(filter_params["SubmitTimeBefore"])

        if filter_obj:
            kwargs["Filter"] = filter_obj

        if "MaxResults" in event and isinstance(event["MaxResults"], int):
            kwargs["MaxResults"] = event["MaxResults"]

        if "NextToken" in event and event["NextToken"]:
            kwargs["NextToken"] = event["NextToken"]

        response = comprehend.list_entities_detection_jobs(**kwargs)
        return json.loads(json.dumps(response, default=json_serial))


    elif operation == "StartEventsDetectionJob":
        # Validate required InputDataConfig.S3Uri
        input_config = event.get("InputDataConfig", {})
        if "S3Uri" not in input_config or not input_config["S3Uri"]:
            return {"Error": "InputDataConfig.S3Uri is required"}

        input_data_config = {
            "S3Uri": input_config["S3Uri"]
        }

        if "InputFormat" in input_config and input_config["InputFormat"]:
            input_data_config["InputFormat"] = input_config["InputFormat"]

        if "DocumentReaderConfig" in input_config and input_config["DocumentReaderConfig"]:
            drc = input_config["DocumentReaderConfig"]
            doc_reader_config = {}

            if "DocumentReadAction" in drc and drc["DocumentReadAction"]:
                doc_reader_config["DocumentReadAction"] = drc["DocumentReadAction"]

            if "DocumentReadMode" in drc and drc["DocumentReadMode"]:
                doc_reader_config["DocumentReadMode"] = drc["DocumentReadMode"]

            if "FeatureTypes" in drc:
                feature_types = [ft for ft in drc["FeatureTypes"] if isinstance(ft, str) and ft.strip()]
                if feature_types:
                    doc_reader_config["FeatureTypes"] = feature_types

            if doc_reader_config:
                input_data_config["DocumentReaderConfig"] = doc_reader_config

        # Validate required OutputDataConfig.S3Uri
        output_config = event.get("OutputDataConfig", {})
        if "S3Uri" not in output_config or not output_config["S3Uri"]:
            return {"Error": "OutputDataConfig.S3Uri is required"}

        output_data_config = {
            "S3Uri": output_config["S3Uri"]
        }

        if "KmsKeyId" in output_config and output_config["KmsKeyId"]:
            output_data_config["KmsKeyId"] = output_config["KmsKeyId"]

        # Start building request kwargs
        kwargs = {
            "InputDataConfig": input_data_config,
            "OutputDataConfig": output_data_config,
            "DataAccessRoleArn": event.get("DataAccessRoleArn"),
            "LanguageCode": event.get("LanguageCode"),
            "TargetEventTypes": event.get("TargetEventTypes", [])
        }

        # Optional fields
        if "ClientRequestToken" in event and isinstance(event["ClientRequestToken"], str) and event["ClientRequestToken"].strip():
            kwargs["ClientRequestToken"] = event["ClientRequestToken"]

        if "JobName" in event and event["JobName"]:
            kwargs["JobName"] = event["JobName"]

        if "Tags" in event and isinstance(event["Tags"], list):
            valid_tags = [tag for tag in event["Tags"] if tag.get("Key") and tag.get("Value")]
            if valid_tags:
                kwargs["Tags"] = valid_tags

        # Call Comprehend API
        response = comprehend.start_events_detection_job(**kwargs)

        return response

    
    elif operation == "StopEventsDetectionJob":
        response = comprehend.stop_events_detection_job(
            JobId=event.get("JobId", "")
        )
        return response
    
    elif operation == "StartFlywheelIteration":
        response = comprehend.start_flywheel_iteration(
            ClientRequestToken=event.get("ClientRequestToken", ""),
            FlywheelArn=event.get("FlywheelArn", "")
        )
        return response
    
    elif operation == "StartKeyPhrasesDetectionJob":
        # Validate required InputDataConfig.S3Uri
        input_config = event.get("InputDataConfig", {})
        if "S3Uri" not in input_config or not input_config["S3Uri"]:
            return {"Error": "InputDataConfig.S3Uri is required"}

        input_data_config = {
            "S3Uri": input_config["S3Uri"]
        }

        if "InputFormat" in input_config and input_config["InputFormat"]:
            input_data_config["InputFormat"] = input_config["InputFormat"]

        if "DocumentReaderConfig" in input_config and input_config["DocumentReaderConfig"]:
            drc = input_config["DocumentReaderConfig"]
            doc_reader_config = {}

            if "DocumentReadAction" in drc and drc["DocumentReadAction"]:
                doc_reader_config["DocumentReadAction"] = drc["DocumentReadAction"]

            if "DocumentReadMode" in drc and drc["DocumentReadMode"]:
                doc_reader_config["DocumentReadMode"] = drc["DocumentReadMode"]

            if "FeatureTypes" in drc:
                feature_types = [ft for ft in drc["FeatureTypes"] if isinstance(ft, str) and ft.strip()]
                if feature_types:
                    doc_reader_config["FeatureTypes"] = feature_types

            if doc_reader_config:
                input_data_config["DocumentReaderConfig"] = doc_reader_config

        # Validate required OutputDataConfig.S3Uri
        output_config = event.get("OutputDataConfig", {})
        if "S3Uri" not in output_config or not output_config["S3Uri"]:
            return {"Error": "OutputDataConfig.S3Uri is required"}

        output_data_config = {
            "S3Uri": output_config["S3Uri"]
        }

        if "KmsKeyId" in output_config and output_config["KmsKeyId"]:
            output_data_config["KmsKeyId"] = output_config["KmsKeyId"]

        # Start building request kwargs
        kwargs = {
            "InputDataConfig": input_data_config,
            "OutputDataConfig": output_data_config,
            "DataAccessRoleArn": event.get("DataAccessRoleArn"),
            "LanguageCode": event.get("LanguageCode")
        }

        # Optional fields
        if "ClientRequestToken" in event and isinstance(event["ClientRequestToken"], str) and event["ClientRequestToken"].strip():
            kwargs["ClientRequestToken"] = event["ClientRequestToken"]

        if "JobName" in event and event["JobName"]:
            kwargs["JobName"] = event["JobName"]

        if "Tags" in event and isinstance(event["Tags"], list):
            valid_tags = [tag for tag in event["Tags"] if tag.get("Key") and tag.get("Value")]
            if valid_tags:
                kwargs["Tags"] = valid_tags

        if "VolumeKmsKeyId" in event and event["VolumeKmsKeyId"]:
            kwargs["VolumeKmsKeyId"] = event["VolumeKmsKeyId"]

        if "VpcConfig" in event and event["VpcConfig"]:
            vpc_config = {}
            if "SecurityGroupIds" in event["VpcConfig"]:
                vpc_config["SecurityGroupIds"] = [sg for sg in event["VpcConfig"]["SecurityGroupIds"] if sg]
            if "Subnets" in event["VpcConfig"]:
                vpc_config["Subnets"] = [sn for sn in event["VpcConfig"]["Subnets"] if sn]
            if vpc_config:
                kwargs["VpcConfig"] = vpc_config

        # Call Comprehend API
        response = comprehend.start_key_phrases_detection_job(**kwargs)

        # Return the response
        return response


    elif operation == "StartPiiEntitiesDetectionJob":
        # Validate required parameters
        if not event.get("DataAccessRoleArn"):
            return {"Error": "DataAccessRoleArn is required"}

        input_config = event.get("InputDataConfig", {})
        if "S3Uri" not in input_config or not input_config["S3Uri"]:
            return {"Error": "InputDataConfig.S3Uri is required"}

        if not event.get("LanguageCode"):
            return {"Error": "LanguageCode is required"}

        if not event.get("Mode"):
            return {"Error": "Mode is required"}

        output_config = event.get("OutputDataConfig", {})
        if "S3Uri" not in output_config or not output_config["S3Uri"]:
            return {"Error": "OutputDataConfig.S3Uri is required"}

        # Build InputDataConfig
        input_data_config = {
            "S3Uri": input_config["S3Uri"]
        }

        if "InputFormat" in input_config and input_config["InputFormat"]:
            input_data_config["InputFormat"] = input_config["InputFormat"]

        if "DocumentReaderConfig" in input_config and input_config["DocumentReaderConfig"]:
            drc = input_config["DocumentReaderConfig"]
            doc_reader_config = {}

            if "DocumentReadAction" in drc and drc["DocumentReadAction"]:
                doc_reader_config["DocumentReadAction"] = drc["DocumentReadAction"]

            if "DocumentReadMode" in drc and drc["DocumentReadMode"]:
                doc_reader_config["DocumentReadMode"] = drc["DocumentReadMode"]

            if "FeatureTypes" in drc:
                feature_types = [ft for ft in drc["FeatureTypes"] if isinstance(ft, str) and ft.strip()]
                if feature_types:
                    doc_reader_config["FeatureTypes"] = feature_types

            if doc_reader_config:
                input_data_config["DocumentReaderConfig"] = doc_reader_config

        # Build OutputDataConfig
        output_data_config = {
            "S3Uri": output_config["S3Uri"]
        }

        if "KmsKeyId" in output_config and output_config["KmsKeyId"]:
            output_data_config["KmsKeyId"] = output_config["KmsKeyId"]

        # Build request
        kwargs = {
            "DataAccessRoleArn": event["DataAccessRoleArn"],
            "InputDataConfig": input_data_config,
            "LanguageCode": event["LanguageCode"],
            "Mode": event["Mode"],
            "OutputDataConfig": output_data_config
        }

        # Optional parameters
        if "ClientRequestToken" in event and isinstance(event["ClientRequestToken"], str) and event["ClientRequestToken"].strip():
            kwargs["ClientRequestToken"] = event["ClientRequestToken"]

        if "JobName" in event and event["JobName"]:
            kwargs["JobName"] = event["JobName"]

        if "RedactionConfig" in event and event["RedactionConfig"]:
            redaction_config = {}
            rc = event["RedactionConfig"]

            if "MaskCharacter" in rc and rc["MaskCharacter"]:
                redaction_config["MaskCharacter"] = rc["MaskCharacter"]

            if "MaskMode" in rc and rc["MaskMode"]:
                redaction_config["MaskMode"] = rc["MaskMode"]

            if "PiiEntityTypes" in rc:
                entity_types = [et for et in rc["PiiEntityTypes"] if isinstance(et, str) and et.strip()]
                if entity_types:
                    redaction_config["PiiEntityTypes"] = entity_types

            if redaction_config:
                kwargs["RedactionConfig"] = redaction_config

        if "Tags" in event and isinstance(event["Tags"], list):
            valid_tags = [tag for tag in event["Tags"] if tag.get("Key") and tag.get("Value")]
            if valid_tags:
                kwargs["Tags"] = valid_tags

        # Call Comprehend API
        response = comprehend.start_pii_entities_detection_job(**kwargs)

        return response

    
    elif operation == "StartSentimentDetectionJob":
        # Validate required InputDataConfig.S3Uri
        input_config = event.get("InputDataConfig", {})
        if "S3Uri" not in input_config or not input_config["S3Uri"]:
            return {"Error": "InputDataConfig.S3Uri is required"}

        input_data_config = {
            "S3Uri": input_config["S3Uri"]
        }

        if "InputFormat" in input_config and input_config["InputFormat"]:
            input_data_config["InputFormat"] = input_config["InputFormat"]

        if "DocumentReaderConfig" in input_config and input_config["DocumentReaderConfig"]:
            drc = input_config["DocumentReaderConfig"]
            doc_reader_config = {}

            if "DocumentReadAction" in drc and drc["DocumentReadAction"]:
                doc_reader_config["DocumentReadAction"] = drc["DocumentReadAction"]

            if "DocumentReadMode" in drc and drc["DocumentReadMode"]:
                doc_reader_config["DocumentReadMode"] = drc["DocumentReadMode"]

            if "FeatureTypes" in drc:
                feature_types = [ft for ft in drc["FeatureTypes"] if isinstance(ft, str) and ft.strip()]
                if feature_types:
                    doc_reader_config["FeatureTypes"] = feature_types

            if doc_reader_config:
                input_data_config["DocumentReaderConfig"] = doc_reader_config

        # Validate required OutputDataConfig.S3Uri
        output_config = event.get("OutputDataConfig", {})
        if "S3Uri" not in output_config or not output_config["S3Uri"]:
            return {"Error": "OutputDataConfig.S3Uri is required"}

        output_data_config = {
            "S3Uri": output_config["S3Uri"]
        }

        if "KmsKeyId" in output_config and output_config["KmsKeyId"]:
            output_data_config["KmsKeyId"] = output_config["KmsKeyId"]

        # Start building request kwargs
        kwargs = {
            "InputDataConfig": input_data_config,
            "OutputDataConfig": output_data_config,
            "DataAccessRoleArn": event.get("DataAccessRoleArn"),
            "LanguageCode": event.get("LanguageCode")
        }

        # Optional fields
        if "ClientRequestToken" in event and isinstance(event["ClientRequestToken"], str) and event["ClientRequestToken"].strip():
            kwargs["ClientRequestToken"] = event["ClientRequestToken"]

        if "JobName" in event and event["JobName"]:
            kwargs["JobName"] = event["JobName"]

        if "Tags" in event and isinstance(event["Tags"], list):
            valid_tags = [tag for tag in event["Tags"] if tag.get("Key") and tag.get("Value")]
            if valid_tags:
                kwargs["Tags"] = valid_tags

        if "VolumeKmsKeyId" in event and event["VolumeKmsKeyId"]:
            kwargs["VolumeKmsKeyId"] = event["VolumeKmsKeyId"]

        if "VpcConfig" in event and event["VpcConfig"]:
            vpc_config = {}
            if "SecurityGroupIds" in event["VpcConfig"]:
                vpc_config["SecurityGroupIds"] = [sg for sg in event["VpcConfig"]["SecurityGroupIds"] if sg]
            if "Subnets" in event["VpcConfig"]:
                vpc_config["Subnets"] = [sn for sn in event["VpcConfig"]["Subnets"] if sn]
            if vpc_config:
                kwargs["VpcConfig"] = vpc_config

        # Call Comprehend API
        response = comprehend.start_sentiment_detection_job(**kwargs)

        # Return response
        return response

    
    elif operation == "StartTargetedSentimentDetectionJob":
        # Validate required InputDataConfig.S3Uri
        input_config = event.get("InputDataConfig", {})
        if "S3Uri" not in input_config or not input_config["S3Uri"]:
            return {"Error": "InputDataConfig.S3Uri is required"}

        input_data_config = {
            "S3Uri": input_config["S3Uri"]
        }

        if "InputFormat" in input_config and input_config["InputFormat"]:
            input_data_config["InputFormat"] = input_config["InputFormat"]

        if "DocumentReaderConfig" in input_config and input_config["DocumentReaderConfig"]:
            drc = input_config["DocumentReaderConfig"]
            doc_reader_config = {}

            if "DocumentReadAction" in drc and drc["DocumentReadAction"]:
                doc_reader_config["DocumentReadAction"] = drc["DocumentReadAction"]

            if "DocumentReadMode" in drc and drc["DocumentReadMode"]:
                doc_reader_config["DocumentReadMode"] = drc["DocumentReadMode"]

            if "FeatureTypes" in drc:
                feature_types = [ft for ft in drc["FeatureTypes"] if isinstance(ft, str) and ft.strip()]
                if feature_types:
                    doc_reader_config["FeatureTypes"] = feature_types

            if doc_reader_config:
                input_data_config["DocumentReaderConfig"] = doc_reader_config

        # Validate required OutputDataConfig.S3Uri
        output_config = event.get("OutputDataConfig", {})
        if "S3Uri" not in output_config or not output_config["S3Uri"]:
            return {"Error": "OutputDataConfig.S3Uri is required"}

        output_data_config = {
            "S3Uri": output_config["S3Uri"]
        }

        if "KmsKeyId" in output_config and output_config["KmsKeyId"]:
            output_data_config["KmsKeyId"] = output_config["KmsKeyId"]

        # Start building request kwargs
        kwargs = {
            "InputDataConfig": input_data_config,
            "OutputDataConfig": output_data_config,
            "DataAccessRoleArn": event.get("DataAccessRoleArn"),
            "LanguageCode": event.get("LanguageCode")
        }

        # Optional fields
        if "ClientRequestToken" in event and isinstance(event["ClientRequestToken"], str) and event["ClientRequestToken"].strip():
            kwargs["ClientRequestToken"] = event["ClientRequestToken"]

        if "JobName" in event and event["JobName"]:
            kwargs["JobName"] = event["JobName"]

        if "Tags" in event and isinstance(event["Tags"], list):
            valid_tags = [tag for tag in event["Tags"] if tag.get("Key") and tag.get("Value")]
            if valid_tags:
                kwargs["Tags"] = valid_tags

        if "VolumeKmsKeyId" in event and event["VolumeKmsKeyId"]:
            kwargs["VolumeKmsKeyId"] = event["VolumeKmsKeyId"]

        if "VpcConfig" in event and event["VpcConfig"]:
            vpc_config = {}
            if "SecurityGroupIds" in event["VpcConfig"]:
                vpc_config["SecurityGroupIds"] = [sg for sg in event["VpcConfig"]["SecurityGroupIds"] if sg]
            if "Subnets" in event["VpcConfig"]:
                vpc_config["Subnets"] = [sn for sn in event["VpcConfig"]["Subnets"] if sn]
            if vpc_config:
                kwargs["VpcConfig"] = vpc_config

        # Call Comprehend API
        response = comprehend.start_targeted_sentiment_detection_job(**kwargs)

        # Return response
        return response

    
    elif operation == "StartTopicsDetectionJob":
        # Validate required InputDataConfig.S3Uri
        input_config = event.get("InputDataConfig", {})
        if "S3Uri" not in input_config or not input_config["S3Uri"]:
            return {"Error": "InputDataConfig.S3Uri is required"}

        input_data_config = {
            "S3Uri": input_config["S3Uri"]
        }

        if "InputFormat" in input_config and input_config["InputFormat"]:
            input_data_config["InputFormat"] = input_config["InputFormat"]

        if "DocumentReaderConfig" in input_config and input_config["DocumentReaderConfig"]:
            drc = input_config["DocumentReaderConfig"]
            doc_reader_config = {}

            if "DocumentReadAction" in drc and drc["DocumentReadAction"]:
                doc_reader_config["DocumentReadAction"] = drc["DocumentReadAction"]

            if "DocumentReadMode" in drc and drc["DocumentReadMode"]:
                doc_reader_config["DocumentReadMode"] = drc["DocumentReadMode"]

            if "FeatureTypes" in drc:
                feature_types = [ft for ft in drc["FeatureTypes"] if isinstance(ft, str) and ft.strip()]
                if feature_types:
                    doc_reader_config["FeatureTypes"] = feature_types

            if doc_reader_config:
                input_data_config["DocumentReaderConfig"] = doc_reader_config

        # Validate required OutputDataConfig.S3Uri
        output_config = event.get("OutputDataConfig", {})
        if "S3Uri" not in output_config or not output_config["S3Uri"]:
            return {"Error": "OutputDataConfig.S3Uri is required"}

        output_data_config = {
            "S3Uri": output_config["S3Uri"]
        }

        if "KmsKeyId" in output_config and output_config["KmsKeyId"]:
            output_data_config["KmsKeyId"] = output_config["KmsKeyId"]

        # Build request parameters
        kwargs = {
            "InputDataConfig": input_data_config,
            "OutputDataConfig": output_data_config,
            "DataAccessRoleArn": event.get("DataAccessRoleArn")
        }

        # Optional fields
        if "ClientRequestToken" in event and isinstance(event["ClientRequestToken"], str) and event["ClientRequestToken"].strip():
            kwargs["ClientRequestToken"] = event["ClientRequestToken"]

        if "JobName" in event and event["JobName"]:
            kwargs["JobName"] = event["JobName"]

        if "NumberOfTopics" in event and isinstance(event["NumberOfTopics"], int) and event["NumberOfTopics"] > 0:
            kwargs["NumberOfTopics"] = event["NumberOfTopics"]

        if "Tags" in event and isinstance(event["Tags"], list):
            valid_tags = [tag for tag in event["Tags"] if tag.get("Key") and tag.get("Value")]
            if valid_tags:
                kwargs["Tags"] = valid_tags

        if "VolumeKmsKeyId" in event and event["VolumeKmsKeyId"]:
            kwargs["VolumeKmsKeyId"] = event["VolumeKmsKeyId"]

        if "VpcConfig" in event and event["VpcConfig"]:
            vpc_config = {}
            if "SecurityGroupIds" in event["VpcConfig"]:
                vpc_config["SecurityGroupIds"] = [sg for sg in event["VpcConfig"]["SecurityGroupIds"] if sg]
            if "Subnets" in event["VpcConfig"]:
                vpc_config["Subnets"] = [sn for sn in event["VpcConfig"]["Subnets"] if sn]
            if vpc_config:
                kwargs["VpcConfig"] = vpc_config

        # Call Comprehend API
        response = comprehend.start_topics_detection_job(**kwargs)

        return response

    elif operation == "ListTopicsDetectionJobs":
        kwargs = {}

        # Handle Filter block
        filter_block = event.get("Filter")
        if filter_block:
            filter_obj = {}

            if "JobName" in filter_block and filter_block["JobName"]:
                filter_obj["JobName"] = filter_block["JobName"]

            if "JobStatus" in filter_block and filter_block["JobStatus"]:
                filter_obj["JobStatus"] = filter_block["JobStatus"]

            if "SubmitTimeAfter" in filter_block and isinstance(filter_block["SubmitTimeAfter"], (int, float)):
                filter_obj["SubmitTimeAfter"] = filter_block["SubmitTimeAfter"]

            if "SubmitTimeBefore" in filter_block and isinstance(filter_block["SubmitTimeBefore"], (int, float)):
                filter_obj["SubmitTimeBefore"] = filter_block["SubmitTimeBefore"]

            if filter_obj:
                kwargs["Filter"] = filter_obj

        # Optional MaxResults
        if "MaxResults" in event and isinstance(event["MaxResults"], int):
            kwargs["MaxResults"] = event["MaxResults"]

        # Optional NextToken
        if "NextToken" in event and isinstance(event["NextToken"], str) and event["NextToken"].strip():
            kwargs["NextToken"] = event["NextToken"]

        # Call the Comprehend API
        response = comprehend.list_topics_detection_jobs(**kwargs)
        return json.loads(json.dumps(response, default=json_serial))

    elif operation == "StopPiiEntitiesDetectionJob":
        response = comprehend.stop_pii_entities_detection_job(
            JobId=event.get("JobId", "")
        )
        return response
    
    elif operation == "StopKeyPhrasesDetectionJob":
        response = comprehend.stop_key_phrases_detection_job(
            JobId=event.get("JobId", "")
        )
        return response

    elif operation == "StopSentimentDetectionJob":
        response = comprehend.stop_sentiment_detection_job(
            JobId=event.get("JobId", "")
        )
        return response

    elif operation == "StopTargetedSentimentDetectionJob":
        response = comprehend.stop_targeted_sentiment_detection_job(
            JobId=event.get("JobId", "")
        )
        return response

    elif operation == "StopTrainingDocumentClassifier":
        response = comprehend.stop_training_document_classifier(
            DocumentClassifierArn=event.get("DocumentClassifierArn", "")
        )
        return response

    elif operation == "StopTrainingEntityRecognizer":
        response = comprehend.stop_training_entity_recognizer(
            EntityRecognizerArn=event.get("EntityRecognizerArn", "")
        )
        return response

    elif operation == "ListDatasets":
        response = comprehend.list_datasets(
            Filter=event.get("Filter", {}),
            FlywheelArn=event.get("FlywheelArn"),
            MaxResults=event.get("MaxResults"),
            NextToken=event.get("NextToken")
        )
        return response

    

    elif operation == "ListEndpoints":
        response = comprehend.list_endpoints(
            Filter=event.get("Filter", {}),
            MaxResults=event.get("MaxResults"),
            NextToken=event.get("NextToken")
        )
        return response


    elif operation == "ListEntityRecognizers":
        response = comprehend.list_entity_recognizers(
            Filter=event.get("Filter", {}),
            MaxResults=event.get("MaxResults"),
            NextToken=event.get("NextToken")
        )
        return response

    elif operation == "ListEntityRecognizerSummaries":
        response = comprehend.list_entity_recognizer_summaries(
            MaxResults=event.get("MaxResults"),
            NextToken=event.get("NextToken")
        )
        return response

    elif operation == "ListEventsDetectionJobs":
        kwargs = {}

        # Handle Filter block
        filter_block = event.get("Filter")
        if filter_block:
            filter_obj = {}

            if "JobName" in filter_block and filter_block["JobName"]:
                filter_obj["JobName"] = filter_block["JobName"]

            if "JobStatus" in filter_block and filter_block["JobStatus"]:
                filter_obj["JobStatus"] = filter_block["JobStatus"]

            if "SubmitTimeAfter" in filter_block and isinstance(filter_block["SubmitTimeAfter"], (int, float)):
                filter_obj["SubmitTimeAfter"] = filter_block["SubmitTimeAfter"]

            if "SubmitTimeBefore" in filter_block and isinstance(filter_block["SubmitTimeBefore"], (int, float)):
                filter_obj["SubmitTimeBefore"] = filter_block["SubmitTimeBefore"]

            if filter_obj:
                kwargs["Filter"] = filter_obj

        # Optional MaxResults
        if "MaxResults" in event and isinstance(event["MaxResults"], int):
            kwargs["MaxResults"] = event["MaxResults"]

        # Optional NextToken
        if "NextToken" in event and isinstance(event["NextToken"], str) and event["NextToken"].strip():
            kwargs["NextToken"] = event["NextToken"]

        # Call the Comprehend API
        response = comprehend.list_events_detection_jobs(**kwargs)
        return json.loads(json.dumps(response, default=json_serial))

    elif operation == "ListKeyPhrasesDetectionJobs":
        kwargs = {}

        # Handle Filter block
        filter_block = event.get("Filter")
        if filter_block:
            filter_obj = {}

            if "JobName" in filter_block and filter_block["JobName"]:
                filter_obj["JobName"] = filter_block["JobName"]

            if "JobStatus" in filter_block and filter_block["JobStatus"]:
                filter_obj["JobStatus"] = filter_block["JobStatus"]

            if "SubmitTimeAfter" in filter_block and isinstance(filter_block["SubmitTimeAfter"], (int, float)):
                filter_obj["SubmitTimeAfter"] = filter_block["SubmitTimeAfter"]

            if "SubmitTimeBefore" in filter_block and isinstance(filter_block["SubmitTimeBefore"], (int, float)):
                filter_obj["SubmitTimeBefore"] = filter_block["SubmitTimeBefore"]

            if filter_obj:
                kwargs["Filter"] = filter_obj

        # Optional MaxResults
        if "MaxResults" in event and isinstance(event["MaxResults"], int):
            kwargs["MaxResults"] = event["MaxResults"]

        # Optional NextToken
        if "NextToken" in event and isinstance(event["NextToken"], str) and event["NextToken"].strip():
            kwargs["NextToken"] = event["NextToken"]

        # Call the Comprehend API
        response = comprehend.list_key_phrases_detection_jobs(**kwargs)
        return json.loads(json.dumps(response, default=json_serial))

    elif operation == "ListPiiEntitiesDetectionJobs":
        kwargs = {}

        # Handle Filter block
        filter_block = event.get("Filter")
        if filter_block:
            filter_obj = {}

            if "JobName" in filter_block and filter_block["JobName"]:
                filter_obj["JobName"] = filter_block["JobName"]

            if "JobStatus" in filter_block and filter_block["JobStatus"]:
                filter_obj["JobStatus"] = filter_block["JobStatus"]

            if "SubmitTimeAfter" in filter_block and isinstance(filter_block["SubmitTimeAfter"], (int, float)):
                filter_obj["SubmitTimeAfter"] = filter_block["SubmitTimeAfter"]

            if "SubmitTimeBefore" in filter_block and isinstance(filter_block["SubmitTimeBefore"], (int, float)):
                filter_obj["SubmitTimeBefore"] = filter_block["SubmitTimeBefore"]

            if filter_obj:
                kwargs["Filter"] = filter_obj

        # Optional MaxResults
        if "MaxResults" in event and isinstance(event["MaxResults"], int):
            kwargs["MaxResults"] = event["MaxResults"]

        # Optional NextToken
        if "NextToken" in event and isinstance(event["NextToken"], str) and event["NextToken"].strip():
            kwargs["NextToken"] = event["NextToken"]

        # Call the Comprehend API
        response = comprehend.list_pii_entities_detection_jobs(**kwargs)
        return json.loads(json.dumps(response, default=json_serial))

    elif operation == "ListSentimentDetectionJobs":
        kwargs = {}

        # Handle Filter block
        filter_block = event.get("Filter")
        if filter_block:
            filter_obj = {}

            if "JobName" in filter_block and filter_block["JobName"]:
                filter_obj["JobName"] = filter_block["JobName"]

            if "JobStatus" in filter_block and filter_block["JobStatus"]:
                filter_obj["JobStatus"] = filter_block["JobStatus"]

            if "SubmitTimeAfter" in filter_block and isinstance(filter_block["SubmitTimeAfter"], (int, float)):
                filter_obj["SubmitTimeAfter"] = filter_block["SubmitTimeAfter"]

            if "SubmitTimeBefore" in filter_block and isinstance(filter_block["SubmitTimeBefore"], (int, float)):
                filter_obj["SubmitTimeBefore"] = filter_block["SubmitTimeBefore"]

            if filter_obj:
                kwargs["Filter"] = filter_obj

        # Optional MaxResults
        if "MaxResults" in event and isinstance(event["MaxResults"], int):
            kwargs["MaxResults"] = event["MaxResults"]

        # Optional NextToken
        if "NextToken" in event and isinstance(event["NextToken"], str) and event["NextToken"].strip():
            kwargs["NextToken"] = event["NextToken"]

        # Call the Comprehend API
        response = comprehend.list_sentiment_detection_jobs(**kwargs)
        return json.loads(json.dumps(response, default=json_serial))

    elif operation == "ListTargetedSentimentDetectionJobs":
        kwargs = {}

        # Handle Filter block
        filter_block = event.get("Filter")
        if filter_block:
            filter_obj = {}

            if "JobName" in filter_block and filter_block["JobName"]:
                filter_obj["JobName"] = filter_block["JobName"]

            if "JobStatus" in filter_block and filter_block["JobStatus"]:
                filter_obj["JobStatus"] = filter_block["JobStatus"]

            if "SubmitTimeAfter" in filter_block and isinstance(filter_block["SubmitTimeAfter"], (int, float)):
                filter_obj["SubmitTimeAfter"] = filter_block["SubmitTimeAfter"]

            if "SubmitTimeBefore" in filter_block and isinstance(filter_block["SubmitTimeBefore"], (int, float)):
                filter_obj["SubmitTimeBefore"] = filter_block["SubmitTimeBefore"]

            if filter_obj:
                kwargs["Filter"] = filter_obj

        # Optional MaxResults
        if "MaxResults" in event and isinstance(event["MaxResults"], int):
            kwargs["MaxResults"] = event["MaxResults"]

        # Optional NextToken
        if "NextToken" in event and isinstance(event["NextToken"], str) and event["NextToken"].strip():
            kwargs["NextToken"] = event["NextToken"]

        # Call the Comprehend API
        response = comprehend.list_targeted_sentiment_detection_jobs(**kwargs)
        return json.loads(json.dumps(response, default=json_serial))

    elif operation == "ListTopicsDetectionJobs":
        response = comprehend.list_topics_detection_jobs(
            Filter=event.get("Filter", {}),
            MaxResults=event.get("MaxResults"),
            NextToken=event.get("NextToken")
        )
        return response

    else:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid operation"})
        }