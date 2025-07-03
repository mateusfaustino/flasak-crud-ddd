from flask import Blueprint, request, jsonify, current_app

from ..services.auth_service import jwt_required

product_bp = Blueprint('product', __name__)


@product_bp.route('/', methods=['GET'])
@jwt_required
def index():
    """Return a JSON list with all stored products."""
    products = current_app.product_service.product_repository.all()
    data = [{'id': p.id, 'name': p.name, 'price': p.price} for p in products]
    return jsonify(data)


@product_bp.route('/<int:product_id>', methods=['GET'])
@jwt_required
def show(product_id):
    """Return details for a single product.

    Parameters
    ----------
    product_id: int
        Identifier of the product to retrieve.

    Returns
    -------
    Response
        JSON representation of the product or a ``404`` message if it does not
        exist.
    """
    product = current_app.product_service.get(product_id)
    if product:
        return jsonify({'id': product.id, 'name': product.name, 'price': product.price})
    return jsonify({'message': 'Not found'}), 404


@product_bp.route('/', methods=['POST'])
@jwt_required
def create():
    """Create a new product from the request JSON body.

    The body must provide ``name`` and ``price`` fields.

    Returns
    -------
    Response
        JSON representation of the new product with a ``201`` status code.
    """
    data = request.get_json() or {}
    product = current_app.product_service.create(data.get('name'), data.get('price'))
    return jsonify({'id': product.id, 'name': product.name, 'price': product.price}), 201


@product_bp.route('/<int:product_id>', methods=['PUT'])
@jwt_required
def update(product_id):
    """Update an existing product using values from the request body.

    Parameters
    ----------
    product_id: int
        Identifier of the product to update.

    Returns
    -------
    Response
        The updated product in JSON format or ``404`` if it does not exist.
    """
    product = current_app.product_service.get(product_id)
    if not product:
        return jsonify({'message': 'Not found'}), 404
    data = request.get_json() or {}
    product = current_app.product_service.update(product, data.get('name'), data.get('price'))
    return jsonify({'id': product.id, 'name': product.name, 'price': product.price})


@product_bp.route('/<int:product_id>', methods=['DELETE'])
@jwt_required
def delete(product_id):
    """Remove a product by its identifier."""
    product = current_app.product_service.get(product_id)
    if not product:
        return jsonify({'message': 'Not found'}), 404
    current_app.product_service.delete(product)
    return jsonify({'message': 'Deleted'})
