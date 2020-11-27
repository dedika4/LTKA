from app.api import bp
from flask import jsonify
from app.models import Position

@bp.route('/positions', methods=['GET'])
def get_position():
	data = Position()
	return jsonify(data.to_dict())

