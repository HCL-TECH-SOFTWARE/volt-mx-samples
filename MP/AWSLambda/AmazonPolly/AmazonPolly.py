import boto3
import json
import base64
from datetime import datetime
import re

# Create a Polly client
client = boto3.client('polly')

# Function to serialize datetime objects into strings
def serialize_datetime(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()  # Convert datetime to ISO 8601 string
    raise TypeError("Type not serializable")

def is_likely_base64(content):
    """Check if a string is likely Base64-encoded"""
    # Base64 strings are typically multiples of 4 characters (with possible padding)
    # and contain only A-Z, a-z, 0-9, +, /, and =
    return bool(re.match(r'^[A-Za-z0-9+/]*={0,2}$', content))

def lambda_handler(event, context):
    action = event.get("action")
    
    try:
        if action == "PutLexicon":
            # Upload Lexicon with automatic format detection
            lexicon_name = event.get("Name")
            content = event.get("Content")
            
            # Auto-detect if the content is Base64 or direct XML
            lexicon_content = content
            content_format = event.get("ContentFormat", "auto")  # Options: "auto", "base64", "xml"
            
            # If content format is auto, try to detect
            if content_format == "auto":
                # If it starts with <?xml or <lexicon, assume it's direct XML
                if content.strip().startswith('<?xml') or content.strip().startswith('<lexicon'):
                    content_format = "xml"
                # Otherwise, if it looks like Base64, try to decode it
                elif is_likely_base64(content):
                    content_format = "base64"
                else:
                    content_format = "xml"  # Default to XML if detection fails
            
            # Handle Base64 format
            if content_format == "base64":
                try:
                    lexicon_content = base64.b64decode(content).decode('utf-8')
                    print("Successfully decoded Base64 content to XML")
                except Exception as e:
                    return {
                        "statusCode": 400,
                        "body": json.dumps({
                            "error": "Base64DecodingError", 
                            "message": f"Failed to decode Base64 content: {str(e)}"
                        })
                    }
            
            # Validate that the content is XML (basic check)
            if not (lexicon_content.strip().startswith('<?xml') or 
                    lexicon_content.strip().startswith('<lexicon')):
                return {
                    "statusCode": 400,
                    "body": json.dumps({
                        "error": "InvalidXMLContent", 
                        "message": "Content does not appear to be valid XML"
                    })
                }
            
            # Print the XML content for debugging
            print(f"XML content to be uploaded: {lexicon_content}")
            
            try:
                # Upload the XML content as lexicon
                response = client.put_lexicon(
                    Name=lexicon_name,
                    Content=lexicon_content
                )
                response['timestamp'] = datetime.now()
                return {
                    "statusCode": 200,
                    "body": json.dumps(response, default=serialize_datetime)
                }
            except client.exceptions.InvalidLexiconException as e:
                # Add more detailed error message
                error_msg = str(e)
                return {
                    "statusCode": 400,
                    "body": json.dumps({
                        "error": "InvalidLexiconException", 
                        "message": error_msg,
                        "xml_content": lexicon_content
                    })
                }

        elif action == "GetLexicon":
            # Get Lexicon
            lexicon_name = event.get("Name")
            response = client.get_lexicon(Name=lexicon_name)
            response['timestamp'] = datetime.now()
            return {
                "statusCode": 200,
                "body": json.dumps(response, default=serialize_datetime)
            }

        elif action == "DeleteLexicon":
            # Delete Lexicon
            lexicon_name = event.get("Name")
            response = client.delete_lexicon(Name=lexicon_name)
            response['timestamp'] = datetime.now()
            return {
                "statusCode": 200,
                "body": json.dumps(response, default=serialize_datetime)
            }

        elif action == "ListLexicons":
            # List all Lexicons
            response = client.list_lexicons()
            response['timestamp'] = datetime.now()
            return {
                "statusCode": 200,
                "body": json.dumps(response, default=serialize_datetime)
            }

        elif action == "SynthesizeSpeech":
            # Synthesize speech
            text = event.get("Text")
            voice_id = event.get("VoiceId", "Joanna")  # Default to Joanna if not provided
            output_format = event.get("OutputFormat", "mp3")  # Default to mp3 if not provided
            response = client.synthesize_speech(
                Text=text,
                VoiceId=voice_id,
                OutputFormat=output_format
            )
            audio_stream = base64.b64encode(response["AudioStream"].read()).decode("utf-8")

            return {
                "statusCode": 200,
                "body": json.dumps({
                    "AudioStream": audio_stream,
                    "ContentType": response.get("ContentType"),
                    "RequestCharacters": response.get("RequestCharacters"),
                    "timestamp": datetime.now().isoformat()
                })
            }


        elif action == "DescribeVoices":
            # Describe voices
            language_code = event.get("LanguageCode", "en-US")  # Default to en-US if not provided
            response = client.describe_voices(
                LanguageCode=language_code
            )
            response['timestamp'] = datetime.now()
            return {
                "statusCode": 200,
                "body": json.dumps(response, default=serialize_datetime)
            }

        elif action == "ListSpeechSynthesisTasks":
            # List synthesis tasks
            response = client.list_speech_synthesis_tasks()
            response['timestamp'] = datetime.now()
            return {
                "statusCode": 200,
                "body": json.dumps(response, default=serialize_datetime)
            }

        elif action == "GetSpeechSynthesisTask":
            # Get synthesis task details
            task_id = event.get("TaskId")
            response = client.get_speech_synthesis_task(TaskId=task_id)
            response['timestamp'] = datetime.now()
            return {
                "statusCode": 200,
                "body": json.dumps(response, default=serialize_datetime)
            }

        else:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Invalid action"})
            }

    except client.exceptions.InvalidLexiconException as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "InvalidLexiconException", "message": str(e)})
        }
    except client.exceptions.LexiconNotFoundException as e:
        return {
            "statusCode": 404,
            "body": json.dumps({"error": "LexiconNotFoundException", "message": str(e)})
        }
    except client.exceptions.LexiconSizeExceededException as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "LexiconSizeExceededException", "message": str(e)})
        }
    except client.exceptions.MaxLexemeLengthExceededException as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "MaxLexemeLengthExceededException", "message": str(e)})
        }
    except client.exceptions.MaxLexiconsNumberExceededException as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "MaxLexiconsNumberExceededException", "message": str(e)})
        }
    except client.exceptions.ServiceFailureException as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "ServiceFailureException", "message": str(e)})
        }
    except client.exceptions.UnsupportedPlsAlphabetException as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "UnsupportedPlsAlphabetException", "message": str(e)})
        }
    except client.exceptions.UnsupportedPlsLanguageException as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "UnsupportedPlsLanguageException", "message": str(e)})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "UnknownError", "message": str(e)})
        }