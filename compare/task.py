class Task(object):
    items = {
        "type": "object",
        "required": ["id", "userId", "name", "testNum", "execNum", "docId",
                     "docName", "type", "timeType", "startTime", "endTime", "orderStartTime",
                     "orderId", "showType"],
        "properties": {
            "id": {
                "type": "int", },
            "userId": {
                "type": "string", },
            "iptNum": {
                "type": "string", },
            "bedNum": {
                "type": "string", },

            "bedSort": {
                "type": "string", },
            "name": {
                "type": "string", },
            "content": {
                "type": "string", },
            "entrust": {
                "type": "string", },

            "testNum": {
                "type": "int", },
            "execNum": {
                "type": "int", },
            "docId": {
                "type": "string", },
            "docName": {
                "type": "string", },
            "deptId": {
                "type": "string", },

            "type": {
                "type": "int", },
            "primayType": {
                "type": "int", },
            "timeType": {
                "type": "string", },
            "startTime": {
                "type": "string", },

            "endTime": {
                "type": "string", },
            "orderStartTime": {
                "type": "string", },
            "orderEndTime": {
                "type": "string", },
            "orderId": {
                "type": "int", },

            "analysisTestNum": {
                "type": "int", },
            "analysisExecNum": {
                "type": "int", },
            "analysisTimeType": {
                "type": "string", },
            "analysisTimeSlot": {
                "type": "string", },
            "showType": {
                "type": "int", },

        }
    }
