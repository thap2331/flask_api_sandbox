from flask import Blueprint, request, jsonify
from utils import DataEndpointsUtils

endpoint = Blueprint('endpoint', __name__)

def ensure_credentials():
    from server.models import Users
    api_key = request.args.get('key')
    limit = request.args.get('limit')
    offset = request.args.get('offset')
    if not api_key:
        return False, "No API key",  limit, offset

    user = Users.query.filter_by(api_key=api_key).first()
    if not user:
        return False, "Incorrect api key",  limit, offset

    enpoint_utils = DataEndpointsUtils()
    if enpoint_utils.api_key_expired(user.api_key_iat):
        return False, 'API key expired',  limit, offset

    if api_key!=user.api_key:
        return False, "Wrong API key.",  limit, offset

    limit=limit if limit else 100
    offset=offset if offset else 0

    return True, '', limit, offset


@endpoint.route('/states', methods=["GET"])
def get_states():

    credentail_check, message, limit, offset = ensure_credentials()
    if credentail_check is True:
        from endpoints.data_models import State, StateSchema
        all_states = State.query.all()
        all_states_data_schema = StateSchema(many=True)
        all_states_data = all_states_data_schema.dump(all_states)
        return jsonify(all_states_data)
    
    return message

@endpoint.route('/categories', methods=["GET"])
def get_categories():

    credentail_check, message, limit, offset = ensure_credentials()
    if credentail_check is True:
        from endpoints.data_models import Categories, CategoriesSchema
        all_states = Categories.query.all()
        all_states_data_schema = CategoriesSchema(many=True)
        all_states_data = all_states_data_schema.dump(all_states)
        return jsonify(all_states_data)
    
    return message

@endpoint.route('/membersbysession', methods=["GET"])
def get_members_by_session():

    credentail_check, message, limit, offset = ensure_credentials()
    if credentail_check is True:
        from endpoints.data_models import MembersBySession, MembersBySessionSchema
        all_states = MembersBySession.query.offset(offset).limit(limit)
        all_states_data_schema = MembersBySessionSchema(many=True)
        all_states_data = all_states_data_schema.dump(all_states)
        return jsonify(all_states_data)
    
    return message

@endpoint.route('/membersaggregate', methods=["GET"])
def get_members_aggregate():

    credentail_check, message, limit, offset = ensure_credentials()
    if credentail_check is True:
        from endpoints.data_models import MembersAggregate, MembersAggregateSchema
        # all_states = MembersAggregate.query.all()
        all_states = MembersAggregate.query.offset(offset).limit(limit)
        all_states_data_schema = MembersAggregateSchema(many=True)
        all_states_data = all_states_data_schema.dump(all_states)
        return jsonify(all_states_data)
    
    return message

@endpoint.route('/sessions', methods=["GET"])
def get_sessions():

    credentail_check, message, limit, offset = ensure_credentials()
    if credentail_check is True:
        from endpoints.data_models import Session, SessionSchema
        all_states = Session.query.all()
        all_states_data_schema = SessionSchema(many=True)
        all_states_data = all_states_data_schema.dump(all_states)
        return jsonify(all_states_data)
    
    return message

@endpoint.route('/bill', methods=["GET"])
def get_bill():

    credentail_check, message, limit, offset = ensure_credentials()
    if credentail_check is True:
        from endpoints.data_models import Bill, BillSchema
        all_states = Bill.query.all()
        all_states_data_schema = BillSchema(many=True)
        all_states_data = all_states_data_schema.dump(all_states)
        return jsonify(all_states_data)
    
    return message

@endpoint.route('/committee', methods=["GET"])
def get_committee():

    credentail_check, message, limit, offset = ensure_credentials()
    if credentail_check is True:
        from endpoints.data_models import Committee, CommitteeSchema
        all_states = Committee.query.all()
        all_states_data_schema = CommitteeSchema(many=True)
        all_states_data = all_states_data_schema.dump(all_states)
        return jsonify(all_states_data)
    
    return message

@endpoint.route('/billhistory', methods=["GET"])
def get_bill_history():

    credentail_check, message, limit, offset = ensure_credentials()
    if credentail_check is True:
        from endpoints.data_models import BillHistory, BillHistorySchema
        all_states = BillHistory.query.all()
        all_states_data_schema = BillHistorySchema(many=True)
        all_states_data = all_states_data_schema.dump(all_states)
        return jsonify(all_states_data)
    
    return message

@endpoint.route('/sponsor', methods=["GET"])
def get_sponsor():

    credentail_check, message, limit, offset = ensure_credentials()
    if credentail_check is True:
        from endpoints.data_models import Sponsor, SponsorSchema
        all_states = Sponsor.query.all()
        all_states_data_schema = SponsorSchema(many=True)
        all_states_data = all_states_data_schema.dump(all_states)
        return jsonify(all_states_data)
    
    return message

@endpoint.route('/floorvote', methods=["GET"])
def get_floorvote():

    credentail_check, message, limit, offset = ensure_credentials()
    if credentail_check is True:
        from endpoints.data_models import FloorVote, FloorVoteSchema
        all_states = FloorVote.query.all()
        all_states_data_schema = FloorVoteSchema(many=True)
        all_states_data = all_states_data_schema.dump(all_states)
        return jsonify(all_states_data)
    
    return message