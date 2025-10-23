import json
import boto3

comprehend_med = boto3.client(service_name='comprehendmedical')

def lambda_handler(event, context):
    text = event.get('Text', '')
    operation = event.get('operation', '')

    if operation == 'DetectEntitiesV2':
        if not text:
            return {
                'statusCode': 400,
                'body': json.dumps('Text input is required for DetectEntitiesV2.')
            }
        response = comprehend_med.detect_entities_v2(Text=text)
    
    elif operation == 'DetectPHI':
        if not text:
            return {
                'statusCode': 400,
                'body': json.dumps('Text input is required for DetectPHI.')
            }
        response = comprehend_med.detect_phi(Text=text)

    elif operation == 'InferICD10CM':
        if not text:
            return {
                'statusCode': 400,
                'body': json.dumps('Text input is required for InferICD10CM.')
            }
        response = comprehend_med.infer_icd10_cm(Text=text)

    elif operation == 'InferRxNorm':
        if not text:
            return {
                'statusCode': 400,
                'body': json.dumps('Text input is required for InferRxNorm.')
            }
        response = comprehend_med.infer_rx_norm(Text=text)

    elif operation == 'InferSNOMEDCT':
        if not text:
            return {
                'statusCode': 400,
                'body': json.dumps('Text input is required for InferSNOMEDCT.')
            }
        response = comprehend_med.infer_snomedct(Text=text)

    elif operation == 'StartEntitiesDetectionV2Job':
        
        data_access_role_arn = event.get('DataAccessRoleArn')
        input_data_config = event.get('InputDataConfig', {})
        input_bucket = input_data_config.get('S3Bucket')
        language_code = event.get('LanguageCode')
        output_data_config = event.get('OutputDataConfig', {})
        output_bucket = output_data_config.get('S3Bucket')
        

        
        missing_fields = []
        if not data_access_role_arn:
            missing_fields.append("DataAccessRoleArn")
        if not input_bucket:
            missing_fields.append("InputDataConfig.S3Bucket")
        if not language_code:
            missing_fields.append("LanguageCode")
        if not output_bucket:
            missing_fields.append("OutputDataConfig.S3Bucket")

        if missing_fields:
            return {
                'statusCode': 400,
                'body': json.dumps(f"Missing required fields: {', '.join(missing_fields)}")
            }

        
        job_request = {
            "DataAccessRoleArn": data_access_role_arn,
            "InputDataConfig": {
                "S3Bucket": input_bucket
            },
            "LanguageCode": language_code,
            "OutputDataConfig": {
                "S3Bucket": output_bucket
            }
            
        }

        
        if input_data_config.get('S3Key'):
            job_request["InputDataConfig"]["S3Key"] = input_data_config['S3Key']

        if output_data_config.get('S3Key'):
            job_request["OutputDataConfig"]["S3Key"] = output_data_config['S3Key']

        if event.get("JobName"):
            job_request["JobName"] = event["JobName"]

        if event.get("KMSKey"):
            job_request["KMSKey"] = event["KMSKey"]

        if event.get("ClientRequestToken"):
            job_request["ClientRequestToken"] = event["ClientRequestToken"]

        response = comprehend_med.start_entities_detection_v2_job(**job_request)
    
    elif operation == 'StartRxNormInferenceJob':
        data_access_role_arn = event.get('DataAccessRoleArn')
        input_data_config = event.get('InputDataConfig', {})
        input_bucket = input_data_config.get('S3Bucket')
        language_code = event.get('LanguageCode')
        output_data_config = event.get('OutputDataConfig', {})
        output_bucket = output_data_config.get('S3Bucket')

        missing_fields = []
        if not data_access_role_arn:
            missing_fields.append("DataAccessRoleArn")
        if not input_bucket:
            missing_fields.append("InputDataConfig.S3Bucket")
        if not language_code:
            missing_fields.append("LanguageCode")
        if not output_bucket:
            missing_fields.append("OutputDataConfig.S3Bucket")

        if missing_fields:
            return {
                'statusCode': 400,
                'body': json.dumps(f"Missing required fields: {', '.join(missing_fields)}")
            }

        job_request = {
            "DataAccessRoleArn": data_access_role_arn,
            "InputDataConfig": {
                "S3Bucket": input_bucket
            },
            "LanguageCode": language_code,
            "OutputDataConfig": {
                "S3Bucket": output_bucket
            }
            
        }

        if input_data_config.get('S3Key'):
            job_request["InputDataConfig"]["S3Key"] = input_data_config['S3Key']
        if output_data_config.get('S3Key'):
            job_request["OutputDataConfig"]["S3Key"] = output_data_config['S3Key']
        if event.get("JobName"):
            job_request["JobName"] = event["JobName"]
        if event.get("KMSKey"):
            job_request["KMSKey"] = event["KMSKey"]
        if event.get("ClientRequestToken"):
            job_request["ClientRequestToken"] = event["ClientRequestToken"]

        response = comprehend_med.start_rx_norm_inference_job(**job_request)
    
    elif operation == 'StartSNOMEDCTInferenceJob':
        data_access_role_arn = event.get('DataAccessRoleArn')
        input_data_config = event.get('InputDataConfig', {})
        input_bucket = input_data_config.get('S3Bucket')
        language_code = event.get('LanguageCode')
        output_data_config = event.get('OutputDataConfig', {})
        output_bucket = output_data_config.get('S3Bucket')

        missing_fields = []
        if not data_access_role_arn:
            missing_fields.append("DataAccessRoleArn")
        if not input_bucket:
            missing_fields.append("InputDataConfig.S3Bucket")
        if not language_code:
            missing_fields.append("LanguageCode")
        if not output_bucket:
            missing_fields.append("OutputDataConfig.S3Bucket")

        if missing_fields:
            return {
                'statusCode': 400,
                'body': json.dumps(f"Missing required fields: {', '.join(missing_fields)}")
            }

        job_request = {
            "DataAccessRoleArn": data_access_role_arn,
            "InputDataConfig": {
                "S3Bucket": input_bucket
            },
            "LanguageCode": language_code,
            "OutputDataConfig": {
                "S3Bucket": output_bucket
            }
            
        }

        if input_data_config.get('S3Key'):
            job_request["InputDataConfig"]["S3Key"] = input_data_config['S3Key']
        if output_data_config.get('S3Key'):
            job_request["OutputDataConfig"]["S3Key"] = output_data_config['S3Key']
        if event.get("JobName"):
            job_request["JobName"] = event["JobName"]
        if event.get("KMSKey"):
            job_request["KMSKey"] = event["KMSKey"]
        if event.get("ClientRequestToken"):
            job_request["ClientRequestToken"] = event["ClientRequestToken"]

        response = comprehend_med.start_snomed_ct_inference_job(**job_request)
    
    elif operation == 'StartICD10CMInferenceJob':
        data_access_role_arn = event.get('DataAccessRoleArn')
        input_data_config = event.get('InputDataConfig', {})
        input_bucket = input_data_config.get('S3Bucket')
        language_code = event.get('LanguageCode')
        output_data_config = event.get('OutputDataConfig', {})
        output_bucket = output_data_config.get('S3Bucket')

        missing_fields = []
        if not data_access_role_arn:
            missing_fields.append("DataAccessRoleArn")
        if not input_bucket:
            missing_fields.append("InputDataConfig.S3Bucket")
        if not language_code:
            missing_fields.append("LanguageCode")
        if not output_bucket:
            missing_fields.append("OutputDataConfig.S3Bucket")

        if missing_fields:
            return {
                'statusCode': 400,
                'body': json.dumps(f"Missing required fields: {', '.join(missing_fields)}")
            }

        job_request = {
            "DataAccessRoleArn": data_access_role_arn,
            "InputDataConfig": {
                "S3Bucket": input_bucket
            },
            "LanguageCode": language_code,
            "OutputDataConfig": {
                "S3Bucket": output_bucket
            },
            
        }

        if input_data_config.get('S3Key'):
            job_request["InputDataConfig"]["S3Key"] = input_data_config['S3Key']
        if output_data_config.get('S3Key'):
            job_request["OutputDataConfig"]["S3Key"] = output_data_config['S3Key']
        if event.get("JobName"):
            job_request["JobName"] = event["JobName"]
        if event.get("KMSKey"):
            job_request["KMSKey"] = event["KMSKey"]
        if event.get("ClientRequestToken"):
            job_request["ClientRequestToken"] = event["ClientRequestToken"]

        response = comprehend_med.start_icd10_cm_inference_job(**job_request)

    elif operation == 'StartPHIDetectionJob':
        data_access_role_arn = event.get('DataAccessRoleArn')
        input_data_config = event.get('InputDataConfig', {})
        input_bucket = input_data_config.get('S3Bucket')
        language_code = event.get('LanguageCode')
        output_data_config = event.get('OutputDataConfig', {})
        output_bucket = output_data_config.get('S3Bucket')

        missing_fields = []
        if not data_access_role_arn:
            missing_fields.append("DataAccessRoleArn")
        if not input_bucket:
            missing_fields.append("InputDataConfig.S3Bucket")
        if not language_code:
            missing_fields.append("LanguageCode")
        if not output_bucket:
            missing_fields.append("OutputDataConfig.S3Bucket")

        if missing_fields:
            return {
                'statusCode': 400,
                'body': json.dumps(f"Missing required fields: {', '.join(missing_fields)}")
            }

        job_request = {
            "DataAccessRoleArn": data_access_role_arn,
            "InputDataConfig": {
                "S3Bucket": input_bucket
            },
            "LanguageCode": language_code,
            "OutputDataConfig": {
                "S3Bucket": output_bucket
            }
        }

        if input_data_config.get('S3Key'):
            job_request["InputDataConfig"]["S3Key"] = input_data_config['S3Key']
        if output_data_config.get('S3Key'):
            job_request["OutputDataConfig"]["S3Key"] = output_data_config['S3Key']
        if event.get("JobName"):
            job_request["JobName"] = event["JobName"]
        if event.get("KMSKey"):
            job_request["KMSKey"] = event["KMSKey"]
        if event.get("ClientRequestToken"):
            job_request["ClientRequestToken"] = event["ClientRequestToken"]

        response = comprehend_med.start_phi_detection_job(**job_request)    
    
    elif operation == 'StopICD10CMInferenceJob':
        job_id = event.get('JobId')
        if not job_id:
            return {
                'statusCode': 400,
                'body': json.dumps('JobId is required for StopICD10CMInferenceJob.')
            }
        response = comprehend_med.stop_icd10_cm_inference_job(JobId=job_id)

    elif operation == 'StopEntitiesDetectionV2Job':
        job_id = event.get('JobId')
        if not job_id:
            return {
                'statusCode': 400,
                'body': json.dumps('JobId is required for StopEntitiesDetectionV2Job.')
            }
        response = comprehend_med.stop_entities_detection_v2_job(JobId=job_id)

    elif operation == 'StopPHIDetectionJob':
        job_id = event.get('JobId')
        if not job_id:
            return {
                'statusCode': 400,
                'body': json.dumps('JobId is required for StopPHIDetectionJob.')
            }
        response = comprehend_med.stop_phi_detection_job(JobId=job_id)

    elif operation == 'StopRxNormInferenceJob':
        job_id = event.get('JobId')
        if not job_id:
            return {
                'statusCode': 400,
                'body': json.dumps('JobId is required for StopRxNormInferenceJob.')
            }
        response = comprehend_med.stop_rx_norm_inference_job(JobId=job_id)

    elif operation == 'StopSNOMEDCTInferenceJob':
        job_id = event.get('JobId')
        if not job_id:
            return {
                'statusCode': 400,
                'body': json.dumps('JobId is required for StopSNOMEDCTInferenceJob.')
            }
        response = comprehend_med.stop_snomed_ct_inference_job(JobId=job_id)
    
    elif operation == 'DescribeEntitiesDetectionV2Job':
        job_id = event.get('JobId')
        if not job_id:
            return {
                'statusCode': 400,
                'body': json.dumps('JobId is required for DescribeEntitiesDetectionV2Job.')
            }
        response = comprehend_med.describe_entities_detection_v2_job(JobId=job_id)

    elif operation == 'DescribeICD10CMInferenceJob':
        job_id = event.get('JobId')
        if not job_id:
            return {
                'statusCode': 400,
                'body': json.dumps('JobId is required for DescribeICD10CMInferenceJob.')
            }
        response = comprehend_med.describe_icd10_cm_inference_job(JobId=job_id)
    
    elif operation == 'DescribePHIDetectionJob':
        job_id = event.get('JobId')
        if not job_id:
            return {
                'statusCode': 400,
                'body': json.dumps('JobId is required for DescribePHIDetectionJob.')
            }
        response = comprehend_med.describe_phi_detection_job(JobId=job_id)

    elif operation == 'DescribeRxNormInferenceJob':
        job_id = event.get('JobId')
        if not job_id:
            return {
                'statusCode': 400,
                'body': json.dumps('JobId is required for DescribeRxNormInferenceJob.')
            }
        response = comprehend_med.describe_rx_norm_inference_job(JobId=job_id)

    elif operation == 'DescribeSNOMEDCTInferenceJob':
        job_id = event.get('JobId')
        if not job_id:
            return {
                'statusCode': 400,
                'body': json.dumps('JobId is required for DescribeSNOMEDCTInferenceJob.')
            }
        response = comprehend_med.describe_snomed_ct_inference_job(JobId=job_id)
    elif operation == 'ListEntitiesDetectionV2Jobs':
    
        list_params = {}
        if "Filter" in event and event["Filter"]:
            list_params["Filter"] = event["Filter"]
        if "MaxResults" in event and event["MaxResults"]:
            list_params["MaxResults"] = event["MaxResults"]
        if "NextToken" in event and event["NextToken"]:
            list_params["NextToken"] = event["NextToken"]
        
        
        response = comprehend_med.list_entities_detection_v2_jobs(**list_params)

    elif operation == 'ListICD10CMInferenceJobs':
        list_params = {
            "Filter": event.get("Filter", {}),
            "MaxResults": event.get("MaxResults", 10),
            "NextToken": event.get("NextToken")
        }
        response = comprehend_med.list_icd10_cm_inference_jobs(**{k: v for k, v in list_params.items() if v is not None})

    elif operation == 'ListPHIDetectionJobs':
        list_params = {
            "Filter": event.get("Filter", {}),
            "MaxResults": event.get("MaxResults", 10),
            "NextToken": event.get("NextToken")
        }
        response = comprehend_med.list_phi_detection_jobs(**{k: v for k, v in list_params.items() if v is not None})

    elif operation == 'ListRxNormInferenceJobs':
        list_params = {
            "Filter": event.get("Filter", {}),
            "MaxResults": event.get("MaxResults", 10),
            "NextToken": event.get("NextToken")
        }
        response = comprehend_med.list_rx_norm_inference_jobs(**{k: v for k, v in list_params.items() if v is not None})

    elif operation == 'ListSNOMEDCTInferenceJobs':
        list_params = {
            "Filter": event.get("Filter", {}),
            "MaxResults": event.get("MaxResults", 10),
            "NextToken": event.get("NextToken")
        }
        response = comprehend_med.list_snomed_ct_inference_jobs(**{k: v for k, v in list_params.items() if v is not None})


    else:
        return {
            'statusCode': 400,
            'body': json.dumps(f'Unknown operation: {operation}')
        }

    return {
        'statusCode': 200,
        'body': json.dumps(response, default=str)
    }
