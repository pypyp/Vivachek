from compare.pageRespanseList import PageRespanseList


class Qc(PageRespanseList):
    items = {
        "type": "object",
        "required": ["id", "value", "sn", "result", "measureTime", "operatorUserName", "paperId", "paperBatchNum",
                     "paperProductionDate", "paperExpiryDate", "liquidId", "liquidBatchNum", "liquidProductionDate",
                     "type", "low", "high"],

        "properties": {
            "id": {
                "type": "integer", },
            "value": {
                "type": "number", },
            "sn": {
                "type": "string",
            },
            "result": {
                "type": "integer", },

            "measureTime": {
                "type": "string", },
            "operatorUserName": {
                "type": "string", },
            "deptName": {
                "type": "string", },
            "paperId": {
                "type": "integer", },

            "paperBatchNum": {
                "type": "string", },
            "paperProductionDate": {
                "type": "string", },
            "paperExpiryDate": {
                "type": "string", },
            "paperOpenTime": {
                "type": "string", },

            "liquidId": {
                "type": "integer", },
            "liquidBatchNum": {
                "type": "string", },
            "liquidProductionDate": {
                "type": "string", },
            "liquidExpiryDate": {
                "type": "string", },

            "liquidOpenTime": {
                "type": "string", },
            "type": {
                "type": "integer", },
            "low": {
                "type": "number", },
            "high": {
                "type": "number", },

        }}

    @staticmethod
    def get():
        Qc.schema["title"] = '质控模块'
        Qc.schema["description"] = '质控列表'

        Qc.schema['properties']['lists']['items'] = Qc.items
        return Qc.schema


