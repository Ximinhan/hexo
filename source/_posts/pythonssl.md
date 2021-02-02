---
title: 使用python ssl问题
date: 2021-01-23 19:25:49
tags:
- atom
- github
- hexo
- travis
categories:
- Diary
---

# SSL 897

Traceback (most recent call last):
  File "/usr/local/lib/python3.6/site-packages/urllib3/connectionpool.py", line 600, in urlopen
    chunked=chunked)
  File "/usr/local/lib/python3.6/site-packages/urllib3/connectionpool.py", line 343, in _make_request
    self._validate_conn(conn)
  File "/usr/local/lib/python3.6/site-packages/urllib3/connectionpool.py", line 839, in _validate_conn
    conn.connect()
  File "/usr/local/lib/python3.6/site-packages/urllib3/connection.py", line 344, in connect
    ssl_context=context)
  File "/usr/local/lib/python3.6/site-packages/urllib3/util/ssl_.py", line 344, in ssl_wrap_socket
    return context.wrap_socket(sock, server_hostname=server_hostname)
  File "/usr/lib64/python3.6/ssl.py", line 365, in wrap_socket
    _context=self, _session=session)
  File "/usr/lib64/python3.6/ssl.py", line 776, in __init__
    self.do_handshake()
  File "/usr/lib64/python3.6/ssl.py", line 1036, in do_handshake
    self._sslobj.do_handshake()
  File "/usr/lib64/python3.6/ssl.py", line 648, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:897)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/ximhan/.local/lib/python3.6/site-packages/requests/adapters.py", line 449, in send
    timeout=timeout
  File "/usr/local/lib/python3.6/site-packages/urllib3/connectionpool.py", line 638, in urlopen
    _stacktrace=sys.exc_info()[2])
  File "/usr/local/lib/python3.6/site-packages/urllib3/util/retry.py", line 398, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='brewhub.engineering.redhat.com', port=443): Max retries exceeded with url: /brewhub (Caused by SSLError(SSLError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:897)'),))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/ximhan/.local/bin/elliott", line 8, in <module>
    sys.exit(main())
  File "/home/ximhan/.local/lib/python3.6/site-packages/elliottlib/cli/__main__.py", line 709, in main
    cli(obj={})
  File "/usr/local/lib/python3.6/site-packages/click/core.py", line 829, in __call__
    return self.main(*args, **kwargs)
  File "/usr/local/lib/python3.6/site-packages/click/core.py", line 782, in main
    rv = self.invoke(ctx)
  File "/usr/local/lib/python3.6/site-packages/click/core.py", line 1259, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File "/usr/local/lib/python3.6/site-packages/click/core.py", line 1066, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/usr/local/lib/python3.6/site-packages/click/core.py", line 610, in invoke
    return callback(*args, **kwargs)
  File "/usr/local/lib/python3.6/site-packages/click/decorators.py", line 73, in new_func
    return ctx.invoke(f, obj, *args, **kwargs)
  File "/usr/local/lib/python3.6/site-packages/click/core.py", line 610, in invoke
    return callback(*args, **kwargs)
  File "/home/ximhan/.local/lib/python3.6/site-packages/elliottlib/cli/verify_attached_operators_cli.py", line 36, in verify_attached_operators_cli
    image_builds = _get_attached_image_builds(brew_session, advisories)
  File "/home/ximhan/.local/lib/python3.6/site-packages/elliottlib/cli/verify_attached_operators_cli.py", line 64, in _get_attached_image_builds
    return [build for build in brew.get_build_objects(build_nvrs, brew_session) if _is_image(build)]
  File "/home/ximhan/.local/lib/python3.6/site-packages/elliottlib/brew.py", line 122, in get_build_objects
    tasks.append(m.getBuild(b))
  File "/usr/local/lib/python3.6/site-packages/koji/__init__.py", line 3247, in __exit__
    self.call_all()
  File "/usr/local/lib/python3.6/site-packages/koji/__init__.py", line 3219, in call_all
    _results = self._session._callMethod('multiCall', args, {})
  File "/usr/local/lib/python3.6/site-packages/koji/__init__.py", line 2787, in _callMethod
    return self._sendCall(handler, headers, request)
  File "/usr/local/lib/python3.6/site-packages/koji/__init__.py", line 2705, in _sendCall
    return self._sendOneCall(handler, headers, request)
  File "/usr/local/lib/python3.6/site-packages/koji/__init__.py", line 2748, in _sendOneCall
    r = self.rsession.post(handler, **callopts)
  File "/home/ximhan/.local/lib/python3.6/site-packages/requests/sessions.py", line 590, in post
    return self.request('POST', url, data=data, json=json, **kwargs)
  File "/home/ximhan/.local/lib/python3.6/site-packages/requests/sessions.py", line 542, in request
    resp = self.send(prep, **send_kwargs)
  File "/home/ximhan/.local/lib/python3.6/site-packages/requests/sessions.py", line 655, in send
    r = adapter.send(request, **kwargs)
  File "/home/ximhan/.local/lib/python3.6/site-packages/requests/adapters.py", line 514, in send
    raise SSLError(e, request=request)
requests.exceptions.SSLError: HTTPSConnectionPool(host='brewhub.engineering.redhat.com', port=443): Max retries exceeded with url: /brewhub (Caused by SSLError(SSLError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:897)'),))


# 解决方法

关闭SSL验证

sudo vim /usr/local/lib/python3.6/site-packages/errata_tool/connector.py
156         if kwargs is not None:
157             if 'data' in kwargs:
158                 ret_data = requests.get(url,
159                                         auth=self._auth,
160                                         data=kwargs['data'],
161                                         verify=self.ssl_verify)
162             elif 'json' in kwargs:
163                 ret_data = requests.get(url,
164                                         auth=self._auth,
165                                         json=kwargs['json'],
166                                         verify=self.ssl_verify)
167             if 'raw' in kwargs:
168                 return_json_decoded_data = not kwargs['raw']
169
170         if ret_data is None:
171             ret_data = requests.get(url, auth=self._auth,
172                                     verify=False)


sudo vim /usr/local/lib/python3.6/site-packages/koji/__init__.py

2745         with warnings.catch_warnings():
2746             warnings.simplefilter("ignore")
2747             r = self.rsession.post(handler, **callopts,verify=False)
2748             r.raise_for_status()
2749             try:
2750                 ret = self._read_xmlrpc_response(r)
2751             finally:
2752                 r.close()
2753         return ret
