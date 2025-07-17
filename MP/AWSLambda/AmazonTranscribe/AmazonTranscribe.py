import json
import boto3
from datetime import datetime

def json_response(status_code, body):
    return {
        "statusCode": status_code,
        "body": json.dumps(body, default=str)
    }

transcribe_client = boto3.client("transcribe",region_name="ap-south-1")

def lambda_handler(event, context):
    print("Incoming Event:", json.dumps(event, indent=2))  # Debugging

    try:
        operation = event.get("operation")

        # Existing operations (unchanged)
        if operation == "StartTranscriptionJob":
            return start_transcription_job(event)
        elif operation == "StartCallAnalyticsJob":
            return start_call_analytics_job(event)
        elif operation == "StartMedicalTranscriptionJob":
            return start_medical_transcription_job(event)
        elif operation == "StartMedicalScribeJob":
            return start_medical_scribe_job(event)
        elif operation == "CreateVocabularyFilter":
            return create_vocabulary_filter(event)
        elif operation == "CreateVocabulary":
            return create_vocabulary(event)
        elif operation == "CreateMedicalVocabulary":
            return create_medical_vocabulary(event)
        elif operation == "CreateLanguageModel":
            return create_language_model(event)
        elif operation == "CreateCallAnalyticsCategory":
            return create_call_analytics_category(event)
        elif operation == "UpdateCallAnalyticsCategory":
            return update_call_analytics_category(event)
        elif operation == "UpdateMedicalVocabulary":
            return update_medical_vocabulary(event)
        elif operation == "UpdateVocabulary":
            return update_vocabulary(event)
        elif operation == "GetTranscriptionJob":
            return get_transcription_job(event)
        elif operation == "GetCallAnalyticsCategory":
            return get_call_analytics_category(event)
        elif operation == "GetCallAnalyticsJob":
            return get_call_analytics_job(event)
        elif operation == "GetMedicalScribeJob":
            return get_medical_scribe_job(event)
        elif operation == "GetMedicalTranscriptionJob":
            return get_medical_transcription_job(event)
        elif operation == "GetMedicalVocabulary":
            return get_medical_vocabulary(event)
        elif operation == "GetVocabulary":
            return get_vocabulary(event)
        elif operation == "GetVocabularyFilter":
            return get_vocabulary_filter(event)
        elif operation == "DeleteTranscriptionJob":
            return delete_transcription_job(event)
        elif operation == "DeleteCallAnalyticsCategory":
            return delete_call_analytics_category(event)
        elif operation == "DeleteCallAnalyticsJob":
            return delete_call_analytics_job(event)
        elif operation == "DeleteLanguageModel":
            return delete_language_model(event)
        elif operation == "DeleteMedicalScribeJob":
            return delete_medical_scribe_job(event)
        elif operation == "DeleteMedicalTranscriptionJob":
            return delete_medical_transcription_job(event)
        elif operation == "DeleteMedicalVocabulary":
            return delete_medical_vocabulary(event)
        elif operation == "DeleteVocabulary":
            return delete_vocabulary(event)
        elif operation == "DeleteVocabularyFilter":
            return delete_vocabulary_filter(event)
        elif operation == "DescribeLanguageModel":
            return describe_language_model(event)
        elif operation == "ListTranscriptionJobs":
            return list_transcription_jobs()
        elif operation == "ListMedicalTranscriptionJobs":
            return list_medical_transcription_jobs(event)
        elif operation == "ListMedicalScribeJobs":
            return list_medical_scribe_jobs(event)
        elif operation == "ListLanguageModels":
            return list_language_models(event)
        elif operation == "ListCallAnalyticsJobs":
            return list_call_analytics_jobs(event)
        elif operation == "ListVocabularyFilters":
            return list_vocabulary_filters(event)
        elif operation == "ListCallAnalyticsCategories":
            return list_call_analytics_categories(event)
        elif operation == "ListMedicalVocabularies":
            return list_medical_vocabularies(event)
        elif operation == "ListVocabularies":
            return list_vocabularies(event)
        elif operation == "ListTagsForResource":
            return list_tags_for_resource(event)
        elif operation == "TagResource":
            return tag_resource(event)
        elif operation == "UntagResource":
            return untag_resource(event)
        else:
            return json_response(400, {"error": "Invalid request format. Missing required keys."})
    
    except Exception as e:
        return json_response(500, {"error": str(e)})

# ✅ Fix: Correct ListTagsForResource Function
def list_tags_for_resource(event):
    try:
        resource_arn = event.get("ResourceArn")
        if not resource_arn:
            return json_response(400, {"error": "Missing required field: ResourceArn"})

        response = transcribe_client.list_tags_for_resource(ResourceArn=resource_arn)
        return json_response(200, {"Tags": response.get("Tags", [])})
    except Exception as e:
        return json_response(500, {"error": str(e)})

# ✅ Fix: Correct ListVocabularies Function
def list_vocabularies(event):
    try:
        response = transcribe_client.list_vocabularies()
        return json_response(200, response.get("Vocabularies", []))

    except Exception as e:
        return json_response(500, {"error": str(e)})
def list_medical_transcription_jobs(event):
    try:
        response = transcribe_client.list_medical_transcription_jobs()
        return json_response(200, response.get("MedicalTranscriptionJobSummaries", []))
    except Exception as e:
        return json_response(500, {"error": str(e)})
def list_medical_scribe_jobs(event):
    try:
        response = transcribe_client.list_medical_scribe_jobs()
        return json_response(200, response.get("MedicalscribeJobSummaries", []))
    except Exception as e:
        return json_response(500, {"error": str(e)})
def list_language_models(event):
    try:
        response = transcribe_client.list_language_models()
        return json_response(200, response.get("Models", []))
    except Exception as e:
        return json_response(500, {"error": str(e)})
def list_call_analytics_jobs(event):
    try:
        response = transcribe_client.list_call_analytics_jobs()
        return json_response(200, response.get("CallAnalyticsJobSummaries", []))
    except Exception as e:
        return json_response(500, {"error": str(e)})
def list_call_analytics_categories(event):
    try:
        response = transcribe_client.list_call_analytics_categories()
        return json_response(200, response.get("Categories", []))
    except Exception as e:
        return json_response(500, {"error": str(e)})
def list_vocabulary_filters(event):
    try:
        response = transcribe_client.list_vocabulary_filters()
        return json_response(200, response.get("VocabularyFilters", []))
    
    except Exception as e:
        return json_response(500, {"error": str(e)})



def list_medical_vocabularies(event):
    try:
        response = transcribe_client.list_medical_vocabularies()
        return json_response(200, response.get("Vocabularies", []))

    except Exception as e:
        return json_response(500, {"error": str(e)})

def start_transcription_job(data):
    try:
        transcription_job_name = data["TranscriptionJobName"]
        media_format = data.get("MediaFormat")
        language_code = data.get("LanguageCode", "en-US")
        
        if "Media" not in data or not isinstance(data["Media"], dict):
            return json_response(400, {"error": "Missing 'Media' object in request."})

        media_file_uri = data["Media"].get("MediaFileUri")
        if not media_file_uri:
            return json_response(400, {"error": "Missing required field: 'MediaFileUri' inside 'Media' object."})

        # Call Transcribe API
        response = transcribe_client.start_transcription_job(
            TranscriptionJobName=transcription_job_name,
            LanguageCode=language_code,
            MediaFormat=media_format,
            Media={"MediaFileUri": media_file_uri}
        )

        job = response.get("TranscriptionJob", {})
        return json_response(200, {"TranscriptionJob": format_transcription_job(job)})
    except Exception as e:
        return json_response(500, {"error": str(e)})
def start_call_analytics_job(event):
    try:
        channel_definitions = event.get("ChannelDefinitions", [])

        # Ensure `ChannelDefinitions` has at least 2 entries
        if not isinstance(channel_definitions, list) or len(channel_definitions) < 2:
            return json_response(400, {
                "error": "ChannelDefinitions must contain at least 2 entries, each with ChannelId and ParticipantRole."
            })

        params = {
            "CallAnalyticsJobName": event.get("CallAnalyticsJobName"),
            "Media": event.get("Media", {}),
            "ChannelDefinitions": channel_definitions
        }

        response = transcribe_client.start_call_analytics_job(**params)
        return json_response(200, {"CallAnalyticsJob": format_call_analytics_job(response)})
    except Exception as e:
        return json_response(500, {"error": str(e)})
def start_medical_transcription_job(event):
    try:
        params = {
            "MedicalTranscriptionJobName": event.get("MedicalTranscriptionJobName"),
            "Media": event.get("Media", {}),
            "LanguageCode": "en-US",  # Fixed required value
            "OutputBucketName": event.get("OutputBucketName"),
            "Specialty": "PRIMARYCARE",  # Fixed required value
            "Type": event.get("Type", "CONVERSATION")  # Default to 'CONVERSATION'
        }

        response = transcribe_client.start_medical_transcription_job(**params)
        return json_response(200, {"MedicalTranscriptionJob": format_medical_transcription_job(response)})
    except Exception as e:
        return json_response(500, {"error": str(e)})
def start_medical_scribe_job(event):
    try:
        settings = event.get("Settings", {})
        channel_definitions = event.get("ChannelDefinitions", [])

        # Ensure that either ShowSpeakerLabels or ChannelIdentification is set to True
        if not (settings.get("ShowSpeakerLabels", False) or settings.get("ChannelIdentification", False)):
            return json_response(400, {
                "error": "Settings must have either ShowSpeakerLabels or ChannelIdentification set to True."
            })
        
        # If ShowSpeakerLabels is True, ensure MaxSpeakerLabels is set
        if settings.get("ShowSpeakerLabels", False) and "MaxSpeakerLabels" not in settings:
            return json_response(400, {
                "error": "MaxSpeakerLabels must be set when ShowSpeakerLabels is True."
            })
        
        # If ChannelIdentification is True, ensure ChannelDefinitions is provided
        if settings.get("ChannelIdentification", False) and len(channel_definitions) < 2:
            return json_response(400, {
                "error": "ChannelDefinitions must contain at least 2 entries when ChannelIdentification is True."
            })

        params = {
            "MedicalScribeJobName": event.get("MedicalScribeJobName"),
            "Media": event.get("Media", {}),
            "OutputBucketName": event.get("OutputBucketName"),
            "DataAccessRoleArn": event.get("DataAccessRoleArn"),
            "Settings": settings,
            "ChannelDefinitions": channel_definitions if settings.get("ChannelIdentification", False) else None
        }

        # Remove None values from params
        params = {k: v for k, v in params.items() if v is not None}

        response = transcribe_client.start_medical_scribe_job(**params)
        return json_response(200, {"MedicalScribeJob": format_medical_scribe_job(response)})
    except Exception as e:
        return json_response(500, {"error": str(e)})
def get_transcription_job(data):
    try:
        transcription_job_name = data["TranscriptionJobName"]
        response = transcribe_client.get_transcription_job(TranscriptionJobName=transcription_job_name)
        job = response.get("TranscriptionJob", {})
        return json_response(200, {"TranscriptionJob": format_transcription_job(job)})
    except Exception as e:
        return json_response(500, {"error": str(e)})
def create_vocabulary_filter(event):
    try:
        params = {
            "VocabularyFilterName": event.get("VocabularyFilterName"),
            "LanguageCode": event.get("LanguageCode"),
        }
        
        if "DataAccessRoleArn" in event:
            params["DataAccessRoleArn"] = event["DataAccessRoleArn"]
        
        if "Tags" in event:
            params["Tags"] = event["Tags"]
        
        if "VocabularyFilterFileUri" in event:
            params["VocabularyFilterFileUri"] = event["VocabularyFilterFileUri"]
        
        if "Words" in event:
            params["Words"] = event["Words"]
        
        response = transcribe_client.create_vocabulary_filter(**params)
        return json_response(200,{"{ }":  format_vocabulary_filter(response)})
    except Exception as e:
        return json_response(500, {"error": str(e)})
def format_vocabulary_filter(response):
    return {
        "LanguageCode": response.get("LanguageCode", ""),
        "LastModifiedTime": response.get("LastModifiedTime", datetime.now()).isoformat(),
        "VocabularyFilterName": response.get("VocabularyFilterName", "")
    }
def create_vocabulary(event):
    try:
        params = {
            "VocabularyName": event.get("VocabularyName"),
            "LanguageCode": event.get("LanguageCode"),
        }
        
        if "DataAccessRoleArn" in event:
            params["DataAccessRoleArn"] = event["DataAccessRoleArn"]
        
        if "Phrases" in event:
            params["Phrases"] = event["Phrases"]
        
        if "Tags" in event:
            params["Tags"] = event["Tags"]
        
        if "VocabularyFileUri" in event:
            params["VocabularyFileUri"] = event["VocabularyFileUri"]
        
        response = transcribe_client.create_vocabulary(**params)
        return json_response(200,{"{ }":  format_vocabulary_response(response)})
    
    except Exception as e:
        return json_response(500, {"error": str(e)})
def format_vocabulary_response(response):
    return {
        "FailureReason": response.get("FailureReason", ""),
        "LanguageCode": response.get("LanguageCode", ""),
        "LastModifiedTime": response.get("LastModifiedTime", datetime.now()).isoformat(),
        "VocabularyName": response.get("VocabularyName", ""),
        "VocabularyState": response.get("VocabularyState", "")
    }
def create_medical_vocabulary(event):
    try:
        params = {
            "VocabularyName": event.get("VocabularyName"),
            "LanguageCode": event.get("LanguageCode"),
            "VocabularyFileUri": event.get("VocabularyFileUri")
        }
        
        if "Tags" in event:
            params["Tags"] = event["Tags"]
        
        response = transcribe_client.create_medical_vocabulary(**params)
        return json_response(200,{"{ }":  format_medical_vocabulary_response(response)})
    
    except Exception as e:
        return json_response(500, {"error": str(e)})
def format_medical_vocabulary_response(response):
    return {
        "FailureReason": response.get("FailureReason", ""),
        "LanguageCode": response.get("LanguageCode", ""),
        "LastModifiedTime": response.get("LastModifiedTime", datetime.now()).isoformat(),
        "VocabularyName": response.get("VocabularyName", ""),
        "VocabularyState": response.get("VocabularyState", "")
    }
def create_language_model(event):
    try:
        params = {
            "ModelName": event.get("ModelName"),
            "BaseModelName": event.get("BaseModelName"),
            "LanguageCode": event.get("LanguageCode"),
            "InputDataConfig": event.get("InputDataConfig", {})
        }
        
        if "Tags" in event:
            params["Tags"] = event["Tags"]
        
        response = transcribe_client.create_language_model(**params)
        return json_response(200,{"{ }":  format_language_model_response(response)})
    
    except Exception as e:
        return json_response(500, {"error": str(e)})
def format_language_model_response(response):
    return {
        "BaseModelName": response.get("BaseModelName", ""),
        "InputDataConfig": response.get("InputDataConfig", {
            "DataAccessRoleArn": "",
            "S3Uri": "",
            "TuningDataS3Uri": ""
        }),
        "LanguageCode": response.get("LanguageCode", ""),
        "ModelName": response.get("ModelName", ""),
        "ModelStatus": response.get("ModelStatus", "")
    }

def create_call_analytics_category(event):
    try:
        params = {
            "CategoryName": event.get("CategoryName"),
            "InputType": event.get("InputType", "POST_CALL"),  # Default to POST_CALL if not provided
            "Rules": event.get("Rules", [])
        }
        
        if "Tags" in event:
            params["Tags"] = event["Tags"]
        
        response = transcribe_client.create_call_analytics_category(**params)
        return json_response(200,{"CategoryProperties":  format_call_analytics_category_response(response)})
    
    except Exception as e:
        return json_response(500, {"error": str(e)})
def format_call_analytics_category_response(response):
    return {
        "CategoryProperties": {
            "CategoryName": response.get("CategoryProperties", {}).get("CategoryName", ""),
            "CreateTime": response.get("CategoryProperties", {}).get("CreateTime", datetime.now()).isoformat(),
            "InputType": response.get("CategoryProperties", {}).get("InputType", ""),
            "LastUpdateTime": response.get("CategoryProperties", {}).get("LastUpdateTime", datetime.now()).isoformat(),
            "Rules": response.get("CategoryProperties", {}).get("Rules", []),
            "Tags": response.get("CategoryProperties", {}).get("Tags", [])
        }
    }
def update_call_analytics_category(event):
    try:
        params = {
            "CategoryName": event.get("CategoryName"),
            "InputType": event.get("InputType", "POST_CALL"),  # Default to POST_CALL if not provided
            "Rules": event.get("Rules", [])
        }
        
        response = transcribe_client.update_call_analytics_category(**params)
        return json_response(200,{"CategoryProperties":  format_updated_call_analytics_category_response(response)})
    
    except Exception as e:
        return json_response(500, {"error": str(e)})
def format_updated_call_analytics_category_response(response):
    return {
        "CategoryProperties": {
            "CategoryName": response.get("CategoryProperties", {}).get("CategoryName", ""),
            "CreateTime": response.get("CategoryProperties", {}).get("CreateTime", datetime.now()).isoformat(),
            "InputType": response.get("CategoryProperties", {}).get("InputType", ""),
            "LastUpdateTime": response.get("CategoryProperties", {}).get("LastUpdateTime", datetime.now()).isoformat(),
            "Rules": response.get("CategoryProperties", {}).get("Rules", []),
            "Tags": response.get("CategoryProperties", {}).get("Tags", [])
        }
    }
def update_medical_vocabulary(event):
    try:
        params = {
            "VocabularyName": event.get("VocabularyName"),
            "LanguageCode": event.get("LanguageCode"),
            "VocabularyFileUri": event.get("VocabularyFileUri")
        }
        
        response = transcribe_client.update_medical_vocabulary(**params)
        return json_response(200,{"":  format_updated_medical_vocabulary_response(response)})
    
    except Exception as e:
        return json_response(500, {"error": str(e)})
def format_updated_medical_vocabulary_response(response):
    return {
        "LanguageCode": response.get("LanguageCode", ""),
        "LastModifiedTime": response.get("LastModifiedTime", datetime.now()).isoformat(),
        "VocabularyName": response.get("VocabularyName", ""),
        "VocabularyState": response.get("VocabularyState", "")
    }
def update_vocabulary(event):
    try:
        params = {
            "VocabularyName": event.get("VocabularyName"),
            "LanguageCode": event.get("LanguageCode")
        }
        
        if "DataAccessRoleArn" in event:
            params["DataAccessRoleArn"] = event["DataAccessRoleArn"]
        
        if "Phrases" in event:
            params["Phrases"] = event["Phrases"]
        
        if "VocabularyFileUri" in event:
            params["VocabularyFileUri"] = event["VocabularyFileUri"]
        
        response = transcribe_client.update_vocabulary(**params)
        return json_response(200,{"":  format_updated_vocabulary_response(response)})
    
    except Exception as e:
        return json_response(500, {"error": str(e)})

def format_updated_vocabulary_response(response):
    return {
        "LanguageCode": response.get("LanguageCode", ""),
        "LastModifiedTime": response.get("LastModifiedTime", datetime.now()).isoformat(),
        "VocabularyName": response.get("VocabularyName", ""),
        "VocabularyState": response.get("VocabularyState", "")
    }
def update_vocabulary_filter(event):
    try:
        params = {
            "VocabularyFilterName": event.get("VocabularyFilterName")
        }
        
        if "DataAccessRoleArn" in event:
            params["DataAccessRoleArn"] = event["DataAccessRoleArn"]
        
        if "VocabularyFilterFileUri" in event:
            params["VocabularyFilterFileUri"] = event["VocabularyFilterFileUri"]
        
        if "Words" in event:
            params["Words"] = event["Words"]
        
        response = transcribe_client.update_vocabulary_filter(**params)
        return json_response(200,{"":  format_updated_vocabulary_filter_response(response)})
    
    except Exception as e:
        return json_response(500, {"error": str(e)})
def format_updated_vocabulary_filter_response(response):
    return {
        "LanguageCode": response.get("LanguageCode", ""),
        "LastModifiedTime": response.get("LastModifiedTime", datetime.now()).isoformat(),
        "VocabularyFilterName": response.get("VocabularyFilterName", "")
    }

def get_call_analytics_category(data):
    try:
        category_name = data["CategoryName"]
        response = transcribe_client.get_call_analytics_category(CategoryName=category_name)
        category = response.get("CategoryProperties", {})
        return json_response(200, {"CategoryProperties": format_category_properties(category)})
    except Exception as e:
        return json_response(500, {"error": str(e)})
def get_call_analytics_job(data):
    try:
        call_analytics_job_name = data["CallAnalyticsJobName"]
        response = transcribe_client.get_call_analytics_job(CallAnalyticsJobName=call_analytics_job_name)
        job_name = response.get("CallAnalyticsJob", {})
        return json_response(200, {"CallAnalyticsJob": format_call_analytics_job(job_name)})
    except Exception as e:
        return json_response(500, {"error": str(e)})
def get_medical_scribe_job(data):
    try:
        medical_scribe_job_name = data["MedicalScribeJobName"]
        response = transcribe_client.get_medical_scribe_job(MedicalScribeJobName=medical_scribe_job_name)
        medicalscribe_job = response.get("MedicalScribeJobName", {})
        return json_response(200, {"MedicalScribeJobName": {}})
    except Exception as e:
        return json_response(500, {"error": str(e)})
def get_medical_transcription_job(data):
    try:
        medical_transcription_job_name = data["MedicalTranscriptionJobName"]
        response = transcribe_client.get_medical_transcription_job(MedicalTranscriptionJobName=medical_transcription_job_name)
        job = response.get("MedicalTranscriptionJob", {})
        return json_response(200, {"MedicalTranscriptionJob": format_medical_transcription_job(job)})
    except Exception as e:
        return json_response(500, {"error": str(e)})
def get_medical_vocabulary(data):
    try:
        vocabulary_name = data["VocabularyName"]
        response = transcribe_client.get_medical_vocabulary(VocabularyName=vocabulary_name)
        vocabulary= response.get("Vocabulary", {})
        return json_response(200, {"Vocabulary": format_medical_vocabulary(vocabulary)})
    except Exception as e:
        return json_response(500, {"error": str(e)})
def get_vocabulary_filter(data):
    try:
        vocabulary_filter_name = data["VocabularyFilterName"]
        response = transcribe_client.get_vocabulary_filter(VocabularyFilterName=vocabulary_filter_name)
        vocabulary= response.get("Vocabulary", {})
        return json_response(200, {"Vocabulary": format_vocabulary_filter(vocabulary)})
    except Exception as e:
        return json_response(500, {"error": str(e)})
def get_vocabulary(data):
    try:
        vocabulary_name = data["VocabularyName"]
        response = transcribe_client.get_medical_vocabulary(VocabularyName=vocabulary_name)
        vocabulary= response.get("Vocabulary", {})
        return json_response(200, {"Vocabulary": format_vocabulary(vocabulary)})
    except Exception as e:
        return json_response(500, {"error": str(e)})


def delete_transcription_job(data):
    try:
        transcription_job_name = data["TranscriptionJobName"]
        transcribe_client.delete_transcription_job(TranscriptionJobName=transcription_job_name)
        return json_response(200, {"message": f"Transcription job '{transcription_job_name}' deleted successfully"})
    except Exception as e:
        return json_response(500, {"error": str(e)})
def delete_call_analytics_category(data):
    try:
        category_name = data["CategoryName"]
        transcribe_client.delete_call_analytics_category(CategoryName=category_name)
        return json_response(200, {"message": f"CategoryName '{category_name}' deleted successfully"})
    except Exception as e:
        return json_response(500, {"error": str(e)})
def delete_call_analytics_job(data):
    try:
        call_analytics_job_name = data["CallAnalyticsJobName"]
        transcribe_client.delete_call_analytics_job(CallAnalyticsJobName=call_analytics_job_name)
        return json_response(200, {"message": f"CallAnalyticsJobName '{call_analytics_job_name}' deleted successfully"})
    except Exception as e:
        return json_response(500, {"error": str(e)})
def delete_language_model(data):
    try:
        model_name = data["ModelName"]
        transcribe_client.delete_language_model(ModelName=model_name)
        return json_response(200, {"message": f"ModelName '{model_name}' deleted successfully"})
    except Exception as e:
        return json_response(500, {"error": str(e)})
def delete_medical_scribe_job(data):
    try:
        medical_scribe_job_name = data["MedicalScribeJobName"]
        transcribe_client.delete_medical_scribe_job(MedicalScribeJobName=medical_scribe_job_name)
        return json_response(200, {"message": f"MedicalScribeJobName '{medical_scribe_job_name}' deleted successfully"})
    except Exception as e:
        return json_response(500, {"error": str(e)})
def delete_medical_transcription_job(data):
    try:
        medical_transcription_job_name = data["MedicalTranscriptionJobName"]
        transcribe_client.delete_medical_transcription_job(MedicalTranscriptionJobName=medical_transcription_job_name)
        return json_response(200, {"message": f"MedicalTranscriptionJobName '{medical_transcription_job_name}' deleted successfully"})
    except Exception as e:
        return json_response(500, {"error": str(e)})
def delete_medical_vocabulary(data):
    try:
        vocabulary_name = data["VocabularyName"]
        transcribe_client.delete_medical_vocabulary(VocabularyName=vocabulary_name)
        return json_response(200, {"message": f"VocabularyName '{vocabulary_name}' deleted successfully"})
    except Exception as e:
        return json_response(500, {"error": str(e)})
def delete_vocabulary(data):
    try:
        vocabulary_name = data["VocabularyName"]
        transcribe_client.delete_vocabulary(VocabularyName=vocabulary_name)
        return json_response(200, {"message": f"VocabularyName '{vocabulary_name}' deleted successfully"})
    except Exception as e:
        return json_response(500, {"error": str(e)})
def delete_vocabulary_filter(data):
    try:
        vocabulary_filter_name = data["VocabularyFilterName"]
        transcribe_client.delete_vocabulary_filter(VocabularyFilterName=vocabulary_filter_name)
        return json_response(200, {"message": f"VocabularyFilterName '{vocabulary_filter_name}' deleted successfully"})
    except Exception as e:
        return json_response(500, {"error": str(e)})
def describe_language_model(data):
    try:
        model_name = data["ModelName"]
        transcribe_client.describe_language_model(ModelName=model_name)
        return json_response(200, response.get("LanguageModel", {}))
    except Exception as e:
        return json_response(500, {"error": str(e)})


def list_transcription_jobs():
    try:
        response = transcribe_client.list_transcription_jobs()
        return json_response(200, response.get("TranscriptionJobSummaries", []))
    except Exception as e:
        return json_response(500, {"error": str(e)})

# ✅ Fix: TagResource & UntagResource with Required Field Checks
def tag_resource(data):
    try:
        if "ResourceArn" not in data or "Tags" not in data:
            return json_response(400, {"error": "Missing required fields: ResourceArn, Tags"})
        
        response = transcribe_client.tag_resource(
            ResourceArn=data["ResourceArn"],
            Tags=data["Tags"]
        )
        
        return json_response(200, {"message": "Tags added successfully"})
    except Exception as e:
        return json_response(500, {"error": str(e)})

def untag_resource(data):
    try:
        if "ResourceArn" not in data or "TagKeys" not in data:
            return json_response(400, {"error": "Missing required fields: ResourceArn, TagKeys"})
        
        response = transcribe_client.untag_resource(
            ResourceArn=data["ResourceArn"],
            TagKeys=data["TagKeys"]
        )
        
        return json_response(200, {"message": "Tags removed successfully"})
    except Exception as e:
        return json_response(500, {"error": str(e)})

def format_transcription_job(job):
    return {
        "CompletionTime": job.get("CompletionTime"),
        "ContentRedaction": job.get("ContentRedaction", {
            "PiiEntityTypes": [],
            "RedactionOutput": "",
            "RedactionType": ""
        }),
        "CreationTime": job.get("CreationTime", datetime.now()).isoformat(),
        "FailureReason": job.get("FailureReason", ""),
        "IdentifiedLanguageScore": job.get("IdentifiedLanguageScore", 0.0),
        "IdentifyLanguage": job.get("IdentifyLanguage", False),
        "IdentifyMultipleLanguages": job.get("IdentifyMultipleLanguages", False),
        "JobExecutionSettings": job.get("JobExecutionSettings", {
            "AllowDeferredExecution": False,
            "DataAccessRoleArn": ""
        }),
        "LanguageCode": job.get("LanguageCode", ""),
        "LanguageCodes": job.get("LanguageCodes", []),
        "LanguageIdSettings": job.get("LanguageIdSettings", {}),
        "LanguageOptions": job.get("LanguageOptions", []),
        "Media": job.get("Media", {
            "MediaFileUri": "",
            "RedactedMediaFileUri": ""
        }),
        "MediaFormat": job.get("MediaFormat", ""),
        "MediaSampleRateHertz": job.get("MediaSampleRateHertz", 0),
        "ModelSettings": job.get("ModelSettings", {
            "LanguageModelName": ""
        }),
        "Settings": job.get("Settings", {
            "ChannelIdentification": False,
            "MaxAlternatives": 0,
            "MaxSpeakerLabels": 0,
            "ShowAlternatives": False,
            "ShowSpeakerLabels": False,
            "VocabularyFilterMethod": "",
            "VocabularyFilterName": "",
            "VocabularyName": ""
        }),
        "StartTime": job.get("StartTime", datetime.now()).isoformat(),
        "Subtitles": job.get("Subtitles", {
            "Formats": [],
            "OutputStartIndex": 0,
            "SubtitleFileUris": []
        }),
        "Tags": job.get("Tags", []),
        "ToxicityDetection": job.get("ToxicityDetection", [{
            "ToxicityCategories": []
        }]),
        "Transcript": job.get("Transcript", {
            "RedactedTranscriptFileUri": "",
            "TranscriptFileUri": ""
        }),
        "TranscriptionJobName": job.get("TranscriptionJobName", ""),
        "TranscriptionJobStatus": job.get("TranscriptionJobStatus", "")
    }
def format_category_properties(category):
    return {
        "CategoryName": category.get("CategoryName", ""),
        "CreateTime": category.get("CreateTime", datetime.now()).isoformat(),
        "InputType": category.get("InputType", ""),
        "LastUpdateTime": category.get("LastUpdateTime", datetime.now()).isoformat(),
        "Rules": category.get("Rules", []),
        "Tags": category.get("Tags", [])
    }
def format_call_analytics_job(job_name):
    return {
        "CallAnalyticsJobName": job_name.get("CallAnalyticsJobName", ""),
        "CallAnalyticsJobStatus": job_name.get("CallAnalyticsJobStatus", ""),
        "ChannelDefinitions": job_name.get("ChannelDefinitions", []),
        "CompletionTime": job_name.get("CompletionTime", datetime.now()).isoformat(),
        "CreationTime": job_name.get("CreationTime", datetime.now()).isoformat(),
        "DataAccessRoleArn": job_name.get("DataAccessRoleArn", ""),
        "FailureReason": job_name.get("FailureReason", ""),
        "IdentifiedLanguageScore": job_name.get("IdentifiedLanguageScore", 0.0),
        "LanguageCode": job_name.get("LanguageCode", ""),
        "Media": job_name.get("Media", {
            "MediaFileUri": "",
            "RedactedMediaFileUri": ""
        }),
        "MediaFormat": job_name.get("MediaFormat", ""),
        "MediaSampleRateHertz": job_name.get("MediaSampleRateHertz", 0),
        "Settings": job_name.get("Settings", {
            "ContentRedaction": {
                "PiiEntityTypes": [],
                "RedactionOutput": "",
                "RedactionType": ""
            },
            "LanguageIdSettings": {},
            "LanguageModelName": "",
            "LanguageOptions": [],
            "Summarization": {
                "GenerateAbstractiveSummary": False
            },
            "VocabularyFilterMethod": "",
            "VocabularyFilterName": "",
            "VocabularyName": ""
        }),
        "StartTime": job_name.get("StartTime", datetime.now()).isoformat(),
        "Tags": job_name.get("Tags", []),
        "Transcript": job_name.get("Transcript", {
            "RedactedTranscriptFileUri": "",
            "TranscriptFileUri": ""
        })
    }
def format_medical_transcription_job(job):
    return {
        "CompletionTime": job.get("CompletionTime", datetime.now()).isoformat(),
        "ContentIdentificationType": job.get("ContentIdentificationType", ""),
        "CreationTime": job.get("CreationTime", datetime.now()).isoformat(),
        "FailureReason": job.get("FailureReason", ""),
        "LanguageCode": job.get("LanguageCode", ""),
        "Media": job.get("Media", {
            "MediaFileUri": "",
            "RedactedMediaFileUri": ""
        }),
        "MediaFormat": job.get("MediaFormat", ""),
        "MediaSampleRateHertz": job.get("MediaSampleRateHertz", 0),
        "MedicalTranscriptionJobName": job.get("MedicalTranscriptionJobName", ""),
        "Settings": job.get("Settings", {
            "ChannelIdentification": False,
            "MaxAlternatives": 0,
            "MaxSpeakerLabels": 0,
            "ShowAlternatives": False,
            "ShowSpeakerLabels": False,
            "VocabularyName": ""
        }),
        "Specialty": job.get("Specialty", ""),
        "StartTime": job.get("StartTime", datetime.now()).isoformat(),
        "Tags": job.get("Tags", []),
        "Transcript": job.get("Transcript", {
            "TranscriptFileUri": ""
        }),
        "TranscriptionJobStatus": job.get("TranscriptionJobStatus", ""),
        "Type": job.get("Type", "")
    }
def format_medical_vocabulary(vocabulary):
    return {
        "DownloadUri": vocabulary.get("DownloadUri", ""),
        "FailureReason": vocabulary.get("FailureReason", ""),
        "LanguageCode": vocabulary.get("LanguageCode", ""),
        "LastModifiedTime": vocabulary.get("LastModifiedTime", datetime.now()).isoformat(),
        "VocabularyName": vocabulary.get("VocabularyName", ""),
        "VocabularyState": vocabulary.get("VocabularyState", "")
    }
def format_vocabulary(vocabulary):
    return {
        "DownloadUri": vocabulary.get("DownloadUri", ""),
        "FailureReason": vocabulary.get("FailureReason", ""),
        "LanguageCode": vocabulary.get("LanguageCode", ""),
        "LastModifiedTime": vocabulary.get("LastModifiedTime", datetime.now()).isoformat(),
        "VocabularyName": vocabulary.get("VocabularyName", ""),
        "VocabularyState": vocabulary.get("VocabularyState", "")
    }
def format_vocabulary_filter(vocabulary):
    return {
        "DownloadUri": vocabulary.get("DownloadUri", ""),
        "LanguageCode": vocabulary.get("LanguageCode", ""),
        "LastModifiedTime": vocabulary.get("LastModifiedTime", datetime.now()).isoformat(),
        "VocabularyFilterName": vocabulary.get("VocabularyName", ""),
    }
def format_call_analytics_job(job):
    return {
        "CallAnalyticsJobDetails": job.get("CallAnalyticsJobDetails", {
            "Skipped": []
        }),
        "CallAnalyticsJobName": job.get("CallAnalyticsJobName", ""),
        "CallAnalyticsJobStatus": job.get("CallAnalyticsJobStatus", ""),
        "ChannelDefinitions": job.get("ChannelDefinitions", []),
        "CompletionTime": job.get("CompletionTime", datetime.now()).isoformat(),
        "CreationTime": job.get("CreationTime", datetime.now()).isoformat(),
        "DataAccessRoleArn": job.get("DataAccessRoleArn", ""),
        "FailureReason": job.get("FailureReason", ""),
        "IdentifiedLanguageScore": job.get("IdentifiedLanguageScore", 0.0),
        "LanguageCode": job.get("LanguageCode", ""),
        "Media": job.get("Media", {
            "MediaFileUri": "",
            "RedactedMediaFileUri": ""
        }),
        "MediaFormat": job.get("MediaFormat", ""),
        "MediaSampleRateHertz": job.get("MediaSampleRateHertz", 0),
        "Settings": job.get("Settings", {
            "ContentRedaction": {
                "PiiEntityTypes": [],
                "RedactionOutput": "",
                "RedactionType": ""
            },
            "LanguageIdSettings": {},
            "LanguageModelName": "",
            "LanguageOptions": [],
            "Summarization": {
                "GenerateAbstractiveSummary": False
            },
            "VocabularyFilterMethod": "",
            "VocabularyFilterName": "",
            "VocabularyName": ""
        }),
        "StartTime": job.get("StartTime", datetime.now()).isoformat(),
        "Tags": job.get("Tags", []),
        "Transcript": job.get("Transcript", {
            "RedactedTranscriptFileUri": "",
            "TranscriptFileUri": ""
        })
    }
def format_medical_transcription_job(job):
    return {
        "CompletionTime": job.get("CompletionTime", datetime.now()).isoformat(),
        "ContentIdentificationType": job.get("ContentIdentificationType", ""),
        "CreationTime": job.get("CreationTime", datetime.now()).isoformat(),
        "FailureReason": job.get("FailureReason", ""),
        "LanguageCode": job.get("LanguageCode", ""),
        "Media": job.get("Media", {
            "MediaFileUri": "",
            "RedactedMediaFileUri": ""
        }),
        "MediaFormat": job.get("MediaFormat", ""),
        "MediaSampleRateHertz": job.get("MediaSampleRateHertz", 0),
        "MedicalTranscriptionJobName": job.get("MedicalTranscriptionJobName", ""),
        "Settings": job.get("Settings", {
            "ChannelIdentification": False,
            "MaxAlternatives": 0,
            "MaxSpeakerLabels": 0,
            "ShowAlternatives": False,
            "ShowSpeakerLabels": False,
            "VocabularyName": ""
        }),
        "Specialty": job.get("Specialty", ""),
        "StartTime": job.get("StartTime", datetime.now()).isoformat(),
        "Tags": job.get("Tags", []),
        "Transcript": job.get("Transcript", {
            "TranscriptFileUri": ""
        }),
        "TranscriptionJobStatus": job.get("TranscriptionJobStatus", ""),
        "Type": job.get("Type", "")
    }
def format_medical_scribe_job(job):
    return {
        "ChannelDefinitions": job.get("ChannelDefinitions", []),
        "CompletionTime": job.get("CompletionTime", datetime.now()).isoformat(),
        "CreationTime": job.get("CreationTime", datetime.now()).isoformat(),
        "DataAccessRoleArn": job.get("DataAccessRoleArn", ""),
        "FailureReason": job.get("FailureReason", ""),
        "LanguageCode": job.get("LanguageCode", ""),
        "Media": job.get("Media", {
            "MediaFileUri": "",
            "RedactedMediaFileUri": ""
        }),
        "MedicalScribeJobName": job.get("MedicalScribeJobName", ""),
        "MedicalScribeJobStatus": job.get("MedicalScribeJobStatus", ""),
        "MedicalScribeOutput": job.get("MedicalScribeOutput", {
            "ClinicalDocumentUri": "",
            "TranscriptFileUri": ""
        }),
        "Settings": job.get("Settings", {
            "ChannelIdentification": False,
            "ClinicalNoteGenerationSettings": {
                "NoteTemplate": ""
            },
            "MaxSpeakerLabels": 0,
            "ShowSpeakerLabels": False,
            "VocabularyFilterMethod": "",
            "VocabularyFilterName": "",
            "VocabularyName": ""
        }),
        "StartTime": job.get("StartTime", datetime.now()).isoformat(),
        "Tags": job.get("Tags", [])
    }
