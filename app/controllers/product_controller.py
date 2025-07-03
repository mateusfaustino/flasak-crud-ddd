from flask import Blueprint, request, jsonify

from ..services.product_service import ProductService
from ..services.auth_service import jwt_required
from ..domain.repositories import ProductRepository

product_bp = Blueprint('product', __name__)


@product_bp.route('/', methods=['GET'])
@jwt_required
def index():
    products = ProductRepository.all()
    data = [{'id': p.id, 'name': p.name, 'price': p.price} for p in products]
    return jsonify(data)


@product_bp.route('/<int:product_id>', methods=['GET'])
@jwt_required
def show(product_id):
    product = ProductRepository.get(product_id)
    if product:
        return jsonify({'id': product.id, 'name': product.name, 'price': product.price})
    return jsonify({'message': 'Not found'}), 404


@product_bp.route('/', methods=['POST'])
@jwt_required
def create():
    data = request.get_json() or {}
    product = ProductService.create(data.get('name'), data.get('price'))
    return jsonify({'id': product.id, 'name': product.name, 'price': product.price}), 201


@product_bp.route('/<int:product_id>', methods=['PUT'])
@jwt_required
def update(product_id):
    product = ProductRepository.get(product_id)
    if not product:
        return jsonify({'message': 'Not found'}), 404
    data = request.get_json() or {}
    product = ProductService.update(product, data.get('name'), data.get('price'))
    return jsonify({'id': product.id, 'name': product.name, 'price': product.price})


@product_bp.route('/<int:product_id>', methods=['DELETE'])
@jwt_required
def delete(product_id):
    product = ProductRepository.get(product_id)
    if not product:
        return jsonify({'message': 'Not found'}), 404
    ProductService.delete(product)
    return jsonify({'message': 'Deleted'})
