from flask import (
    Blueprint, flash,  render_template, request, url_for
)
from flaskr.predict import pre
from werkzeug.utils import secure_filename
import os


bp = Blueprint('classis', __name__)


@bp.route("/")
def index():
    return render_template('classis/index.html')


@bp.route('/upload', methods=['GET', 'POST'])
def upload():
    pre_result = False
    if request.method == 'POST':
        f = request.files.get('file')
        error = None

        if not f:
            error = "请上传图片！"

        if error is not None:
            flash(error)

        # 进行预测操作
        else:
            filename = secure_filename(f.filename)
            path = "flaskr/static/user_images/{}".format(filename)
            f.save(path)
            # pre_path = 'flaskr/static/user_images/{}'.format(filename)
            pre_result = pre(path)
            return render_template('classis/upload.html', pre=pre_result)

            os.remove("static/user_images/"+filename)

    return render_template('classis/upload.html', pre=pre_result)




