"""
         /**
            * 质控分析接口数据格式校验
            */

    """


class Analysis():
    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "title": '质控模块',
        "description": '质控分析',
        "type": "object",
        "required": ["coefficientOfVariation", "qcRecords", "standardDeviation", "targetValue"],
        "properties": {
            "coefficientOfVariation": {"type": "number"},
            "standardDeviation": {"type": "number"},
            "targetValue": {"type": "number"},
            "qcRecords": {"type": "array",
                          "items": {
                              "type": "object",
                              "required": ["id", "value", "sn", "result", "measureTime",
                                           "operatorUserName", "paperId", "paperBatchNum",
                                           "paperProductionDate", "paperExpiryDate", "liquidId",
                                           "liquidBatchNum", "liquidProductionDate",
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

                                  "liquidId": {
                                      "type": "integer", },
                                  "liquidBatchNum": {
                                      "type": "string", },
                                  "liquidProductionDate": {
                                      "type": "string", },
                                  "liquidExpiryDate": {
                                      "type": "string", },

                                  "type": {
                                      "type": "integer", },
                                  "low": {
                                      "type": "number", },
                                  "high": {
                                      "type": "number", },

                              },
                          }
                          },

        },

    }
