����������: http://209.141.51.211:8888/d0ff431b
�
���������: http://209.141.51.211:8888/d0ff431b
username: bkttmiex
password: 5c632e40


root
6c7efe86eb54c744


Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/django/core/handlers/exception.py", line 34, in inner
    response = get_response(request)
  File "/usr/lib/python3/dist-packages/django/core/handlers/base.py", line 115, in _get_response
    response = self.process_exception_by_middleware(e, request)
  File "/usr/lib/python3/dist-packages/django/core/handlers/base.py", line 113, in _get_response
    response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "/root/Dapp-django/app/views.py", line 54, in result
    context=getOrder(address)
  File "/root/Dapp-django/app/getToken.py", line 274, in getOrder
    print(newFromDict)
UnicodeEncodeError: 'latin-1' codec can't encode character '\u2620' in position 20861: ordinal not in range(256)