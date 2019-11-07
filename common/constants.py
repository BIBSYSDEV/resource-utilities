class Constants:
    ENV_VAR_REGION = 'REGION'
    ENV_VAR_TABLE_NAME = 'TABLE_NAME'

    EVENT_BODY = 'body'
    EVENT_HTTP_METHOD = 'httpMethod'
    EVENT_PATH_PARAMETERS = 'pathParameters'
    EVENT_PATH_PARAMETER_IDENTIFIER = 'identifier'
    EVENT_RESOURCE_IDENTIFIER = 'resource_identifier'

    HTTP_METHOD_GET = 'GET'
    HTTP_METHOD_POST = 'POST'
    HTTP_METHOD_PUT = 'PUT'

    JSON_ATTRIBUTE_NAME_RESOURCE = 'resource'

    RESPONSE_STATUS_CODE = 'statusCode'
    RESPONSE_BODY = 'body'
    RESPONSE_HEADERS = 'headers'

    DDB = 'dynamodb'
    DDB_RESPONSE_ATTRIBUTE_NAME_ITEMS = 'Items'
    DDB_RESPONSE_ATTRIBUTE_NAME_RESPONSE_METADATA = 'ResponseMetadata'
    DDB_RESPONSE_ATTRIBUTE_NAME_RESPONSE_HTTP_STATUS_CODE = 'HTTPStatusCode'

    DDB_FIELD_RESOURCE_IDENTIFIER = 'resource_identifier'
    DDB_FIELD_MODIFIED_DATE = 'modifiedDate'
    DDB_FIELD_CREATED_DATE = 'createdDate'
    DDB_FIELD_METADATA = 'metadata'
    DDB_FIELD_FILES = 'files'
    DDB_FIELD_OWNER = 'owner'

    ERROR_MISSING_EVENT = 'Missing event'
    ERROR_INSUFFICIENT_PARAMETERS = 'Insufficient parameters'
