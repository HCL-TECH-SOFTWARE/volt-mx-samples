import json
import boto3
import base64

textract = boto3.client('textract')

def lambda_handler(event, context):
    def missing_required_parameter(param):
        return {"statusCode": 400, "body": json.dumps({"error": f"Missing required parameter: {param}"})}

    try:
        operation_type = event.get('operation')
        if not operation_type:
            return missing_required_parameter("operation")

        def get_document_parameter():
            document_base64 = event.get("document")
            s3_bucket = event.get("s3_bucket")
            s3_key = event.get("s3_key")
            s3_version = event.get("s3_version")
            if document_base64:
                return {"Bytes": base64.b64decode(document_base64)}
            elif s3_bucket and s3_key:
                s3_object = {"Bucket": s3_bucket, "Name": s3_key}
                if s3_version:
                    s3_object["Version"] = s3_version
                return {"S3Object": s3_object}
            return None

        # AnalyzeDocument
        if operation_type == 'analyze_document':
            document = get_document_parameter()
            feature_types = event.get("FeatureTypes")
            if not document or not feature_types:
                return missing_required_parameter("document and FeatureTypes")
            params = {"Document": document, "FeatureTypes": feature_types}
            if "QueriesConfig" in event:
                params["QueriesConfig"] = event["QueriesConfig"]
            if "AdaptersConfig" in event:
                params["AdaptersConfig"] = event["AdaptersConfig"]
            if "HumanLoopConfig" in event:
                params["HumanLoopConfig"] = event["HumanLoopConfig"]
            return textract.analyze_document(**params)

        #  AnalyzeExpense
        elif operation_type == 'analyze_expense':
            document = get_document_parameter()
            if not document:
                return missing_required_parameter("document")
            return textract.analyze_expense(Document=document)

        #  AnalyzeID
        elif operation_type == 'analyze_id':
            document = get_document_parameter()
            if not document:
                return missing_required_parameter("document")
            return textract.analyze_id(DocumentPages=[document])

        # CreateAdapter
        elif operation_type == 'create_adapter':
            name = event.get("AdapterName")
            features = event.get("FeatureTypes")
            if not name or not features:
                return missing_required_parameter("AdapterName and FeatureTypes")
            params = {"AdapterName": name, "FeatureTypes": features}
            for optional in ["AutoUpdate", "ClientRequestToken", "Description", "Tags"]:
                if optional in event:
                    params[optional] = event[optional]
            return textract.create_adapter(**params)

        #  CreateAdapterVersion
        elif operation_type == 'create_adapter_version':
            aid, bucket, key, out_cfg = event.get("AdapterId"), event.get("s3_bucket"), event.get("s3_key"), event.get("OutputConfig")
            if not aid or not bucket or not key or not out_cfg or not out_cfg.get("S3Bucket"):
                return missing_required_parameter("AdapterId, s3_bucket, s3_key, OutputConfig.S3Bucket")
            params = {
                "AdapterId": aid,
                "DatasetConfig": {"ManifestS3Object": {"Bucket": bucket, "Name": key}},
                "OutputConfig": {"S3Bucket": out_cfg["S3Bucket"]}
            }
            if "S3Prefix" in out_cfg:
                params["OutputConfig"]["S3Prefix"] = out_cfg["S3Prefix"]
            for optional in ["ClientRequestToken", "KMSKeyId"]:
                if optional in event:
                    params[optional] = event[optional]
            return textract.create_adapter_version(**params)

        #  DeleteAdapter
        elif operation_type == 'delete_adapter':
            aid = event.get("AdapterId")
            if not aid:
                return missing_required_parameter("AdapterId")
            return textract.delete_adapter(AdapterId=aid)

        #  DeleteAdapterVersion
        elif operation_type == 'delete_adapter_version':
            aid, ver = event.get("AdapterId"), event.get("AdapterVersion")
            if not aid or not ver:
                return missing_required_parameter("AdapterId and AdapterVersion")
            return textract.delete_adapter_version(AdapterId=aid, AdapterVersion=ver)

        #  DetectDocumentText
        elif operation_type == 'detect_document_text':
            doc = get_document_parameter()
            if not doc:
                return missing_required_parameter("document")
            return textract.detect_document_text(Document=doc)

        #  GetAdapter
        elif operation_type == 'get_adapter':
            aid = event.get("AdapterId")
            if not aid:
                return missing_required_parameter("AdapterId")
            return textract.get_adapter(AdapterId=aid)

        #  GetAdapterVersion
        elif operation_type == 'get_adapter_version':
            aid, ver = event.get("AdapterId"), event.get("AdapterVersion")
            if not aid or not ver:
                return missing_required_parameter("AdapterId and AdapterVersion")
            return textract.get_adapter_version(AdapterId=aid, AdapterVersion=ver)

        #  GetDocumentAnalysis
        elif operation_type == 'get_document_analysis':
            jid = event.get("JobId")
            if not jid:
                return missing_required_parameter("JobId")
            return textract.get_document_analysis(JobId=jid, MaxResults=event.get("MaxResults"), NextToken=event.get("NextToken"))

        #  GetDocumentTextDetection
        elif operation_type == 'get_document_text_detection':
            jid = event.get("JobId")
            if not jid:
                return missing_required_parameter("JobId")
            return textract.get_document_text_detection(JobId=jid, MaxResults=event.get("MaxResults"), NextToken=event.get("NextToken"))

        #  GetExpenseAnalysis
        elif operation_type == 'get_expense_analysis':
            jid = event.get("JobId")
            if not jid:
                return missing_required_parameter("JobId")
            return textract.get_expense_analysis(JobId=jid, MaxResults=event.get("MaxResults"), NextToken=event.get("NextToken"))

        #  GetLendingAnalysis
        elif operation_type == 'get_lending_analysis':
            jid = event.get("JobId")
            if not jid:
                return missing_required_parameter("JobId")
            return textract.get_lending_analysis(JobId=jid, MaxResults=event.get("MaxResults"), NextToken=event.get("NextToken"))

        #  GetLendingAnalysisSummary
        elif operation_type == 'get_lending_analysis_summary':
            jid = event.get("JobId")
            if not jid:
                return missing_required_parameter("JobId")
            return textract.get_lending_analysis_summary(JobId=jid)

        #  ListAdapters
        elif operation_type == 'list_adapters':
            params = {k: event[k] for k in ["AfterCreationTime", "BeforeCreationTime", "MaxResults", "NextToken"] if k in event}
            return textract.list_adapters(**params)

        #  ListAdapterVersions
        elif operation_type == 'list_adapter_versions':
            aid = event.get("AdapterId")
            if not aid:
                return missing_required_parameter("AdapterId")
            params = {"AdapterId": aid}
            for k in ["AfterCreationTime", "BeforeCreationTime", "MaxResults", "NextToken"]:
                if k in event:
                    params[k] = event[k]
            return textract.list_adapter_versions(**params)

        #  StartDocumentAnalysis
        elif operation_type == 'start_document_analysis':
            doc_loc = event.get("DocumentLocation")
            features = event.get("FeatureTypes")
            if not doc_loc or not features:
                return missing_required_parameter("DocumentLocation and FeatureTypes")
            params = {"DocumentLocation": doc_loc, "FeatureTypes": features}
            for k in ["ClientRequestToken", "JobTag", "NotificationChannel", "OutputConfig", "KMSKeyId", "QueriesConfig", "AdaptersConfig"]:
                if k in event:
                    params[k] = event[k]
            return textract.start_document_analysis(**params)

        #  StartDocumentTextDetection
        elif operation_type == 'start_document_text_detection':
            doc_loc = event.get("DocumentLocation")
            if not doc_loc:
                return missing_required_parameter("DocumentLocation")
            params = {"DocumentLocation": doc_loc}
            for k in ["ClientRequestToken", "JobTag", "NotificationChannel", "OutputConfig", "KMSKeyId"]:
                if k in event:
                    params[k] = event[k]
            return textract.start_document_text_detection(**params)

        #  StartExpenseAnalysis
        elif operation_type == 'start_expense_analysis':
            doc_loc = event.get("DocumentLocation")
            out_cfg = event.get("OutputConfig")
            if not doc_loc or not out_cfg:
                return missing_required_parameter("DocumentLocation and OutputConfig")
            params = {"DocumentLocation": doc_loc, "OutputConfig": out_cfg}
            for k in ["ClientRequestToken", "JobTag", "NotificationChannel", "KMSKeyId"]:
                if k in event:
                    params[k] = event[k]
            return textract.start_expense_analysis(**params)

        #  StartLendingAnalysis
        elif operation_type == 'start_lending_analysis':
            doc_loc = event.get("DocumentLocation")
            out_cfg = event.get("OutputConfig")
            if not doc_loc or not out_cfg:
                return missing_required_parameter("DocumentLocation and OutputConfig")
            params = {"DocumentLocation": doc_loc, "OutputConfig": out_cfg}
            for k in ["ClientRequestToken", "JobTag", "NotificationChannel", "KMSKeyId"]:
                if k in event:
                    params[k] = event[k]
            return textract.start_lending_analysis(**params)

        #  TagResource
        elif operation_type == 'tag_resource':
            arn, tags = event.get("ResourceARN"), event.get("Tags")
            if not arn or not tags:
                return missing_required_parameter("ResourceARN and Tags")
            return textract.tag_resource(ResourceArn=arn, Tags=tags)

        #  UntagResource
        elif operation_type == 'untag_resource':
            arn, tag_keys = event.get("ResourceARN"), event.get("TagKeys")
            if not arn or not tag_keys:
                return missing_required_parameter("ResourceARN and TagKeys")
            return textract.untag_resource(ResourceArn=arn, TagKeys=tag_keys)
        
        elif operation_type == 'list_tags_for_resource':
            arn = event.get("ResourceARN")
            if not arn:
                return missing_required_parameter("ResourceARN")
            return textract.list_tags_for_resource(ResourceArn=arn)
        
        #  UpdateAdapter
        elif operation_type == 'update_adapter':
            aid = event.get("AdapterId")
            if not aid:
                return missing_required_parameter("AdapterId")
            params = {"AdapterId": aid}
            for k in ["AdapterName", "AutoUpdate", "Description"]:
                if k in event:
                    params[k] = event[k]
            return textract.update_adapter(**params)

        else:
            return {"statusCode": 400, "body": json.dumps({"error": f"Invalid operation: {operation_type}"})}

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
