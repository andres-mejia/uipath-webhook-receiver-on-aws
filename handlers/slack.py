# -*- coding: utf-8 -*-
import gettext
import json
import os
import uipath
from urlparse import parse_qs


def handler(event, context):
    params = parse_qs(event["body"])

    token = params["token"][0]
    if token != os.environ["verification_token"]:
        message = _("Request token does not match")
        response = {"statusCode": 403, "error": message}
        return response

    process_name = None
    if "text" in params:
        process_name = params["text"][0]

    available_processes = [
        s.strip() for s in os.environ["available_processes"].split(',')
    ]
    if (not process_name or process_name not in available_processes):
        message = _("Available process name are {}").format(
            ", ".join(available_processes))
        response = {"statusCode": 200, "body": message}
        return response

    message = uipath.start_jobs(process_name)
    response = {"statusCode": 200, "body": message}
    return response
