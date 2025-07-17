import boto3
import json

lex_models_client = boto3.client('lexv2-models')
lex_runtime_client = boto3.client('lexv2-runtime')

def lambda_handler(event, context):
    operation_name = event.get("operation_name")

    try:
        # Lex Models V2 Operations
        if operation_name == "create_bot":
            response = lex_models_client.create_bot(
                botName=event["botName"],
                roleArn=event["roleArn"],
                dataPrivacy=event["dataPrivacy"],
                idleSessionTTLInSeconds=event["idleSessionTTLInSeconds"]
            )

        elif operation_name == "create_intent":
            response = lex_models_client.create_intent(
                intentName=event["intentName"],
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"]
            )

        elif operation_name == "create_slot_type":
            response = lex_models_client.create_slot_type(
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"],
                slotTypeName=event["slotTypeName"],
                slotTypeValues=event["slotTypeValues"],
                valueSelectionSetting=event["valueSelectionSetting"]
            )

        elif operation_name == "batch_create_custom_vocabulary_item":
            response = lex_models_client.batch_create_custom_vocabulary_item(
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"],
                customVocabularyItemList=event["customVocabularyItemList"]
            )

        elif operation_name == "batch_delete_custom_vocabulary_item":
            response = lex_models_client.batch_delete_custom_vocabulary_item(
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"],
                customVocabularyItemList=event["customVocabularyItemList"]
            )

        elif operation_name == "batch_update_custom_vocabulary_item":
            response = lex_models_client.batch_update_custom_vocabulary_item(
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"],
                customVocabularyItemList=event["customVocabularyItemList"]
            )

        elif operation_name == "build_bot_locale":
            response = lex_models_client.build_bot_locale(
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"]
            )

        elif operation_name == "create_bot_alias":
            response = lex_models_client.create_bot_alias(
                botAliasName=event["botAliasName"],
                botId=event["botId"],
                botVersion=event["botVersion"]
            )

        elif operation_name == "create_bot_locale":
            response = lex_models_client.create_bot_locale(
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"],
                nluIntentConfidenceThreshold=event["nluIntentConfidenceThreshold"]
            )

        elif operation_name == "create_bot_replica":
            response = lex_models_client.create_bot_replica(
                sourceBotId=event["sourceBotId"],
                replicaRegion=event["replicaRegion"]
            )

        elif operation_name == "create_bot_version":
            response = lex_models_client.create_bot_version(
                botId=event["botId"],
                description=event.get("description")
            )

        elif operation_name == "create_export":
            response = lex_models_client.create_export(
                resourceSpecification=event["resourceSpecification"],
                fileFormat=event["fileFormat"]
            )

        # Additional Lex Models V2 Operations
        elif operation_name == "create_resource_policy":
            response = lex_models_client.create_resource_policy(
                resourceArn=event["resourceArn"],
                policy=event["policy"]
            )

        elif operation_name == "create_resource_policy_statement":
            response = lex_models_client.create_resource_policy_statement(
                resourceArn=event["resourceArn"],
                statementId=event["statementId"],
                effect=event["effect"],
                principal=event["principal"],
                action=event["action"],
                condition=event.get("condition")
            )

        elif operation_name == "create_slot":
            response = lex_models_client.create_slot(
                slotName=event["slotName"],
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"],
                intentId=event["intentId"],
                valueElicitationSetting=event["valueElicitationSetting"]
            )

        elif operation_name == "create_upload_url":
            response = lex_models_client.create_upload_url()
        

        elif operation_name == "delete_bot":
            response = lex_models_client.delete_bot(
                botId=event["botId"],
                skipResourceInUseCheck=event.get("skipResourceInUseCheck", False)
            )

        elif operation_name == "delete_bot_alias":
            response = lex_models_client.delete_bot_alias(
                botId=event["botId"],
                botAliasId=event["botAliasId"],
                skipResourceInUseCheck=event.get("skipResourceInUseCheck", False)
            )

        elif operation_name == "delete_bot_locale":
            response = lex_models_client.delete_bot_locale(
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"]
            )

        elif operation_name == "delete_bot_version":
            response = lex_models_client.delete_bot_version(
                botId=event["botId"],
                botVersion=event["botVersion"]
            )

        elif operation_name == "delete_custom_vocabulary":
            response = lex_models_client.delete_custom_vocabulary(
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"]
            )

        elif operation_name == "delete_export":
            response = lex_models_client.delete_export(
                exportId=event["exportId"]
            )

        elif operation_name == "delete_import":
            response = lex_models_client.delete_import(
                importId=event["importId"]
            )

        elif operation_name == "delete_intent":
            response = lex_models_client.delete_intent(
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"],
                intentId=event["intentId"]
            )

        elif operation_name == "delete_resource_policy":
            response = lex_models_client.delete_resource_policy(
                resourceArn=event["resourceArn"]
            )

        elif operation_name == "delete_resource_policy_statement":
            response = lex_models_client.delete_resource_policy_statement(
                resourceArn=event["resourceArn"],
                statementId=event["statementId"],
                expectedRevisionId=event.get("expectedRevisionId")
            )

        elif operation_name == "delete_slot":
            response = lex_models_client.delete_slot(
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"],
                intentId=event["intentId"],
                slotId=event["slotId"]
            )

        elif operation_name == "delete_slot_type":
            response = lex_models_client.delete_slot_type(
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"],
                slotTypeId=event["slotTypeId"]
            )

        elif operation_name == "describe_bot":
            response = lex_models_client.describe_bot(
                botId=event["botId"]
            )

        elif operation_name == "describe_bot_alias":
            response = lex_models_client.describe_bot_alias(
                botId=event["botId"],
                botAliasId=event["botAliasId"]
            )

        elif operation_name == "describe_bot_locale":
            response = lex_models_client.describe_bot_locale(
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"]
            )

        elif operation_name == "describe_bot_recommendation":
            response = lex_models_client.describe_bot_recommendation(
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"],
                botRecommendationId=event["botRecommendationId"]
            )

        elif operation_name == "describe_bot_version":
            response = lex_models_client.describe_bot_version(
                botId=event["botId"],
                botVersion=event["botVersion"]
            )

        elif operation_name == "describe_custom_vocabulary_metadata":
            response = lex_models_client.describe_custom_vocabulary_metadata(
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"]
            )

        elif operation_name == "describe_export":
            response = lex_models_client.describe_export(
                exportId=event["exportId"]
            )

        elif operation_name == "describe_import":
            response = lex_models_client.describe_import(
                importId=event["importId"]
            )

        elif operation_name == "describe_intent":
            response = lex_models_client.describe_intent(
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"],
                intentId=event["intentId"]
            )

        elif operation_name == "describe_resource_policy":
            response = lex_models_client.describe_resource_policy(
                resourceArn=event["resourceArn"]
            )

        elif operation_name == "describe_slot":
            response = lex_models_client.describe_slot(
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"],
                intentId=event["intentId"],
                slotId=event["slotId"]
            )

        elif operation_name == "describe_slot_type":
            response = lex_models_client.describe_slot_type(
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"],
                slotTypeId=event["slotTypeId"]
            )

        elif operation_name == "generate_bot_template":
            response = lex_models_client.generate_bot_template(
                botName=event["botName"],
                botType=event["botType"],
                language=event["language"]
            )

        elif operation_name == "get_bot_recommendation":
            response = lex_models_client.get_bot_recommendation(
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"],
                botRecommendationId=event["botRecommendationId"]
            )

        elif operation_name == "get_custom_vocabulary":
            response = lex_models_client.get_custom_vocabulary(
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"]
            )

        elif operation_name == "list_aggregated_utterances":
            response = lex_models_client.list_aggregated_utterances(
                botId=event["botId"],
                botAliasId=event.get("botAliasId"),
                botVersion=event.get("botVersion"),
                localeId=event["localeId"],
                filters=event.get("filters"),
                maxResults=event.get("maxResults"),
                nextToken=event.get("nextToken")
            )

        elif operation_name == "list_bot_aliases":
            response = lex_models_client.list_bot_aliases(
                botId=event["botId"],
            )

        elif operation_name == "list_bot_locales":
            response = lex_models_client.list_bot_locales(
                botId=event["botId"],
                botVersion=event["botVersion"],
                filters=event.get("filters"),
                maxResults=event.get("maxResults"),
                nextToken=event.get("nextToken")
            )

        elif operation_name == "list_bot_recommendations":
            response = lex_models_client.list_bot_recommendations(
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"],
                maxResults=event.get("maxResults"),
                nextToken=event.get("nextToken")
            )

        elif operation_name == "list_bot_replicas":
            response = lex_models_client.list_bot_replicas(
                botId=event["botId"],
                maxResults=event.get("maxResults"),
                nextToken=event.get("nextToken")
            )

        elif operation_name == "list_bot_versions":
            response = lex_models_client.list_bot_versions(
                botId=event["botId"],
                maxResults=event.get("maxResults"),
                nextToken=event.get("nextToken")
            )

        elif operation_name == "list_bots":
            response = lex_models_client.list_bots(
              
            )

        elif operation_name == "list_built_in_intents":
            response = lex_models_client.list_built_in_intents(
                localeId=event["localeId"],
                sortBy=event.get("sortBy"),
                maxResults=event.get("maxResults"),
                nextToken=event.get("nextToken")
            )

        elif operation_name == "list_built_in_slot_types":
            response = lex_models_client.list_built_in_slot_types(
                localeId=event["localeId"],
                sortBy=event.get("sortBy"),
                maxResults=event.get("maxResults"),
                nextToken=event.get("nextToken")
            )

        elif operation_name == "list_custom_vocabulary_items":
            response = lex_models_client.list_custom_vocabulary_items(
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"],
                maxResults=event.get("maxResults"),
                nextToken=event.get("nextToken")
            )

        elif operation_name == "list_exports":
            response = lex_models_client.list_exports(
                filters=event.get("filters"),
                sortBy=event.get("sortBy"),
                maxResults=event.get("maxResults"),
                nextToken=event.get("nextToken")
            )

        elif operation_name == "list_imports":
            response = lex_models_client.list_imports(
                filters=event.get("filters"),
                sortBy=event.get("sortBy"),
                maxResults=event.get("maxResults"),
                nextToken=event.get("nextToken")
            )

        elif operation_name == "list_intents":
            response = lex_models_client.list_intents(
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"],
                filters=event.get("filters"),
                sortBy=event.get("sortBy"),
                maxResults=event.get("maxResults"),
                nextToken=event.get("nextToken")
            )

        elif operation_name == "list_recommended_intents":
            response = lex_models_client.list_recommended_intents(
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"],
                botRecommendationId=event["botRecommendationId"],
                maxResults=event.get("maxResults"),
                nextToken=event.get("nextToken")
            )

        elif operation_name == "list_slot_types":
            response = lex_models_client.list_slot_types(
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"],
                filters=event.get("filters"),
                sortBy=event.get("sortBy"),
                maxResults=event.get("maxResults"),
                nextToken=event.get("nextToken")
            )

        elif operation_name == "list_slots":
            response = lex_models_client.list_slots(
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"],
                intentId=event["intentId"],
                filters=event.get("filters"),
                sortBy=event.get("sortBy"),
                maxResults=event.get("maxResults"),
                nextToken=event.get("nextToken")
            )

        elif operation_name == "list_tags_for_resource":
            response = lex_models_client.list_tags_for_resource(
                resourceARN=event["resourceARN"]
            )

        elif operation_name == "search_associated_transcripts":
            response = lex_models_client.search_associated_transcripts(
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"],
                searchOrder=event.get("searchOrder"),
                filters=event["filters"],
                maxResults=event.get("maxResults"),
                nextToken=event.get("nextToken")
            )

        elif operation_name == "start_bot_recommendation":
            response = lex_models_client.start_bot_recommendation(
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"],
                transcriptSourceSetting=event["transcriptSourceSetting"]
            )

        elif operation_name == "start_import":
            response = lex_models_client.start_import(
                importId=event["importId"],
                resourceSpecification=event["resourceSpecification"],
                mergeStrategy=event["mergeStrategy"]
            )

        elif operation_name == "stop_bot_recommendation":
            response = lex_models_client.stop_bot_recommendation(
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"],
                botRecommendationId=event["botRecommendationId"]
            )

        elif operation_name == "tag_resource":
            response = lex_models_client.tag_resource(
                resourceARN=event["resourceARN"],
                tags=event["tags"]
            )

        elif operation_name == "untag_resource":
            response = lex_models_client.untag_resource(
                resourceARN=event["resourceARN"],
                tagKeys=event["tagKeys"]
            )

        elif operation_name == "update_bot":
            response = lex_models_client.update_bot(
                botId=event["botId"],
                botName=event["botName"],
                dataPrivacy=event["dataPrivacy"],
                roleArn=event["roleArn"],
                idleSessionTTLInSeconds=event["idleSessionTTLInSeconds"],
                testBotAliasTags=event.get("testBotAliasTags")
            )

        elif operation_name == "update_bot_alias":
            response = lex_models_client.update_bot_alias(
                botAliasId=event["botAliasId"],
                botId=event["botId"],
                botAliasName=event["botAliasName"],
                description=event.get("description"),
                botVersion=event.get("botVersion"),
                sentimentAnalysisSettings=event.get("sentimentAnalysisSettings"),
                conversationLogSettings=event.get("conversationLogSettings")
            )

        elif operation_name == "update_bot_locale":
            response = lex_models_client.update_bot_locale(
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"],
                nluIntentConfidenceThreshold=event["nluIntentConfidenceThreshold"],
                description=event.get("description")
            )

        elif operation_name == "update_bot_recommendation":
            response = lex_models_client.update_bot_recommendation(
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"],
                botRecommendationId=event["botRecommendationId"],
                encryptionSetting=event.get("encryptionSetting")
            )

        elif operation_name == "update_export":
            response = lex_models_client.update_export(
                exportId=event["exportId"],
                filePassword=event["filePassword"]
            )

        elif operation_name == "update_intent":
            response = lex_models_client.update_intent(
                intentId=event["intentId"],
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"],
                intentName=event["intentName"],
                description=event.get("description"),
                parentIntentSignature=event.get("parentIntentSignature"),
                sampleUtterances=event.get("sampleUtterances"),
                dialogCodeHook=event.get("dialogCodeHook"),
                fulfillmentCodeHook=event.get("fulfillmentCodeHook"),
                slotPriorities=event.get("slotPriorities"),
                intentConfirmationSetting=event.get("intentConfirmationSetting"),
                intentClosingSetting=event.get("intentClosingSetting"),
                inputContexts=event.get("inputContexts"),
                outputContexts=event.get("outputContexts"),
                kendraConfiguration=event.get("kendraConfiguration"),
                initialResponseSetting=event.get("initialResponseSetting")
            )

        elif operation_name == "update_resource_policy":
            response = lex_models_client.update_resource_policy(
                resourceArn=event["resourceArn"],
                policy=event["policy"],
                expectedRevisionId=event.get("expectedRevisionId")
            )

        elif operation_name == "update_slot":
            response = lex_models_client.update_slot(
                slotId=event["slotId"],
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"],
                intentId=event["intentId"],
                slotName=event["slotName"],
                description=event.get("description"),
                slotTypeId=event.get("slotTypeId"),
                valueElicitationSetting=event["valueElicitationSetting"],
                obfuscationSetting=event.get("obfuscationSetting"),
                multipleValuesSetting=event.get("multipleValuesSetting")
            )

        elif operation_name == "update_slot_type":
            response = lex_models_client.update_slot_type(
                slotTypeId=event["slotTypeId"],
                botId=event["botId"],
                botVersion=event["botVersion"],
                localeId=event["localeId"],
                slotTypeName=event["slotTypeName"],
                description=event.get("description"),
                slotTypeValues=event.get("slotTypeValues"),
                valueSelectionSetting=event.get("valueSelectionSetting"),
                parentSlotTypeSignature=event.get("parentSlotTypeSignature"),
                compositeSlotTypeSetting=event.get("compositeSlotTypeSetting")
            )

        # Lex Runtime V2 Operations
        elif operation_name == "recognize_text":
            recognize_text_args = {
                "botId": event["botId"],
                "botAliasId": event["botAliasId"],
                "localeId": event["localeId"],
                "sessionId": event["sessionId"],
                "text": event["text"]
            }

            if "sessionState" in event and isinstance(event["sessionState"], dict):
                recognize_text_args["sessionState"] = event["sessionState"]
            if "requestAttributes" in event and isinstance(event["requestAttributes"], dict):
                recognize_text_args["requestAttributes"] = event["requestAttributes"]

            response = lex_runtime_client.recognize_text(**recognize_text_args)

        elif operation_name == "get_session":
            response = lex_runtime_client.get_session(
                botId=event["botId"],
                botAliasId=event["botAliasId"],
                localeId=event["localeId"],
                sessionId=event["sessionId"]
            )

        elif operation_name == "delete_session":
            response = lex_runtime_client.delete_session(
                botId=event["botId"],
                botAliasId=event["botAliasId"],
                localeId=event["localeId"],
                sessionId=event["sessionId"]
            )

        elif operation_name == "put_session":
            response = lex_runtime_client.put_session(
                botId=event["botId"],
                botAliasId=event["botAliasId"],
                localeId=event["localeId"],
                sessionId=event["sessionId"],
                messages=event["messages"],
                sessionState=event["sessionState"],
                responseContentType=event["responseContentType"]
            )

        elif operation_name == "recognize_utterance":
            input_stream = event["inputStream"].encode("utf-8")  # Convert string to bytes
            response = lex_runtime_client.recognize_utterance(
                botId=event["botId"],
                botAliasId=event["botAliasId"],
                localeId=event["localeId"],
                sessionId=event["sessionId"],
                requestContentType=event["requestContentType"],
                responseContentType=event["responseContentType"],
                inputStream=input_stream
            )


        # Additional Lex Runtime operations
        elif operation_name == "start_conversation":
            response = lex_runtime_client.start_conversation(
                botId=event["botId"],
                botAliasId=event["botAliasId"],
                localeId=event["localeId"],
                sessionId=event["sessionId"],
                sessionState=event.get("sessionState"),
                requestAttributes=event.get("requestAttributes")
            )

        # Pagination and Waiters
        elif operation_name == "can_paginate":
            can_paginate = lex_runtime_client.can_paginate(event["operation"])
            response = {"can_paginate": can_paginate}

        elif operation_name == "get_paginator":
            paginator = lex_runtime_client.get_paginator(event["paginatorName"])
            response = {"message": "Paginator retrieved successfully."}

        elif operation_name == "get_waiter":
            waiter = lex_runtime_client.get_waiter(event["waiterName"])
            response = {"message": "Waiter retrieved successfully."}

        elif operation_name == "close":
            lex_runtime_client.close()
            response = {"message": "Client closed."}

        else:
            response = {"error": f"Unsupported operation_name: {operation_name}"}

        return {
            "statusCode": 200,
            "body": json.dumps(response, default=str)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e),
                "event": event
            })
        }
