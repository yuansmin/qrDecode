# -*- coding: utf-8 -*-
# @Date    : 2016-11-30 11:12:44
# @Author  : fancy (fancy@thecover.cn)

import json
import qrtools
import urlparse
import requests

from flask import Flask, request

app = Flask('decoder')


@app.route('/decode', methods=['GET'])
def decode_img():
    try:
        result = {'status': 0, 'is_qr': False, 'data': None, 'msg': 'success'}
        url = request.args.get('url', None)
        file_name = 'images/qr'
        if url:
            domain = urlparse.urlsplit(url).netloc
            headers = {'Referer': domain}
            resp = requests.get(url, headers=headers)
            with open(file_name, 'w') as f:
                f.write(resp.content)
        else:
            file = request.files['file']
            file.save('images/qr')
        qr = qrtools.QR()
        result['is_qr'] = qr.decode(file_name)
        if result['is_qr']:
            result['data'] = qr.data
    except Exception, e:
        result['status'] = 1
        result['msg'] = str(e)
    finally:
        return json.dumps(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8002')
