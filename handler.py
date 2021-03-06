# -*- coding: utf-8 -*-
import gettext
import json
import logging
import os

languages = [os.environ["language"]]
trans = gettext.translation(
    "messages", localedir="locale", languages=languages, fallback=True)
trans.install()


def handler_wrapper(func):
    def decorate(event, context):
        try:
            log = logging.getLogger()
            log.setLevel(logging.DEBUG)
            log.debug("Received event {}".format(json.dumps(event)))
            log.debug("Received body {}".format(
                json.dumps(json.loads(event["body"]))))
        except:
            pass
        response = func(event, context)
        log.debug("Response {}".format(json.dumps(response)))
        return response

    return decorate


@handler_wrapper
def backlog_handler(event, context):
    import handlers.backlog
    response = handlers.backlog.handler(event, context)
    return response


@handler_wrapper
def github_handler(event, context):
    import handlers.github
    response = handlers.github.handler(event, context)
    return response


@handler_wrapper
def google_hangouts_handler(event, context):
    import handlers.google_hangouts
    response = handlers.google_hangouts.handler(event, context)
    return response


@handler_wrapper
def html_form_handler(event, context):
    import handlers.html_form
    response = handlers.html_form.handler(event, context)
    return response


@handler_wrapper
def iot_button_handler(event, context):
    import handlers.iot_button
    response = handlers.iot_button.handler(event, context)
    return response


@handler_wrapper
def orchestrator_handler(event, context):
    import handlers.orchestrator
    response = handlers.orchestrator.handler(event, context)
    return response


@handler_wrapper
def slack_handler(event, context):
    import handlers.slack
    response = handlers.slack.handler(event, context)
    return response


@handler_wrapper
def wrike_handler(event, context):
    import handlers.wrike
    response = handlers.wrike.handler(event, context)
    return response