from app import db, ma
from sqlalchemy import Column, Date, ForeignKey, Integer, SmallInteger, String, Table, Text
from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship

class State(db.Model):
    __tablename__ = 'states'

    state = db.Column(db.String(30))
    state_id = db.Column(db.String(2), primary_key=True)
    legislature_name = db.Column(db.String(200))
    upper_chamber_name = db.Column(db.String(200))
    lower_chamber_name = db.Column(db.String(200))
    bicameral = db.Column(db.SmallInteger)
    lower_chamber_members = db.Column(db.SmallInteger)
    upper_chamber_members = db.Column(db.SmallInteger)
    statehood_date = db.Column(db.Date)

    # all_sessions = relationship('Session', backref='State')

class StateSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = State
        load_instance = True

class Categories(db.Model):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    category_type = Column(String(200))
    status = Column(Integer)
    category_string = Column(String(200))

class CategoriesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Categories
        load_instance = True

class MembersAggregate(db.Model):
    __tablename__ = 'members_aggregate'

    member_id = Column(String(8), primary_key=True)
    last_name = Column(String(150))
    given_name = Column(String(150))
    suffix = Column(String(10))
    alternate_names = Column(String(150))
    # state = Column(ForeignKey('states.state_id'), index=True)
    state = Column(String(30))
    upper_chamber = Column(TINYINT)
    lower_chamber = Column(TINYINT)
    upper_chamber_terms = Column(TINYINT)
    upper_chamber_years = Column(TINYINT)
    lower_chamber_terms = Column(TINYINT)
    lower_chamber_years = Column(TINYINT)
    all_parties = Column(String(200))
    all_districts = Column(String(500))
    all_counties = Column(String(300))
    all_committees = Column(String(1200))
    affiliations = Column(String(500))
    leadership_positions = Column(String(500))
    total_terms = Column(TINYINT)
    total_years = Column(TINYINT)
    other_offices_held = Column(String(500))
    education = Column(String(1000))
    occupations = Column(String(1000))
    race_ethnicity = Column(String(100))
    gender = Column(String(10))
    birth_day = Column(TINYINT)
    birth_month = Column(TINYINT)
    birth_year = Column(SmallInteger)
    birthplace = Column(String(150))
    death_day = Column(TINYINT)
    death_month = Column(TINYINT)
    death_year = Column(SmallInteger)
    place_of_death = Column(String(150))
    # multiple_state_id = Column(ForeignKey('members_aggregate.member_id'), index=True)
    multiple_state_id = Column(String(2))
    links = Column(String(300))
    all_cities_of_residence = Column(String(100))
    notes = Column(String(2000))
    appointed_first = Column(TINYINT)
    religion = Column(String(100))
    relatives_in_govt = Column(String(500))
    wiki_link = Column(String(300))

#     # multiple_state = relationship('MembersAggregate', remote_side=[member_id])
#     # state1 = relationship('State')

class MembersAggregateSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MembersAggregate
        load_instance = True

class Session(db.Model):
    __tablename__ = 'sessions'

    session_id = Column(String(15), primary_key=True)
    session_name = Column(String(100))
    # state = Column(String(30), ForeignKey('states.state_id'))
    state = Column(String(30))
    year = Column(SmallInteger)
    legislature_num = Column(SmallInteger)
    start_date = Column(Date)
    end_date = Column(Date)
    notes = Column(String(300))
    session_type = Column(String(15))
    upper_majority_party = Column(String(50))
    lower_majority_party = Column(String(50))
    session_subname = Column(String(60))
    state_status = Column(TINYINT)


class SessionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Session
        load_instance = True

class Bill(db.Model):
    __tablename__ = 'bills'

    bill_id = Column(String(100), primary_key=True)
    # session_id = Column(ForeignKey('sessions.session_id'), index=True)
    session_id = Column(String(15))
    state_bill_number = Column(String(50))
    year = Column(SmallInteger)
    state = Column(String(30))
    state_topics = Column(Text)
    federal_topics = Column(Text)
    hsp_tags = Column(Text)
    state_description = Column(Text)
    final_action = Column(Text)
    final_aggregate_votes = Column(Text)
    bill_type = Column(String(100))
    originating_chamber = Column(String(5))
    link = Column(Text)
    amended = Column(TINYINT)
    notes = Column(Text)

class BillSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Bill
        load_instance = True


class Committee(db.Model):
    __tablename__ = 'committees'

    committee_id = Column(String(15), primary_key=True)
    committee_name = Column(String)
    # session_id = Column(ForeignKey('sessions.session_id'), index=True)
    session_id = Column(String(15))
    year = Column(SmallInteger)
    size = Column(SmallInteger)
    chamber = Column(String(5))
    hsp_category = Column(String(200))

class CommitteeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Committee
        load_instance = True

class MembersBySession(db.Model):
    __tablename__ = 'members_by_session'

    member_session_id = Column(String(20), primary_key=True)
    last_name = Column(String(150))
    given_name = Column(String(150))
    suffix = Column(String(10))
    year = Column(SmallInteger)
    state = db.Column(db.String(30))
    session_id = Column(String(15))
    static_member_id = Column(String(8))
    # state = Column(ForeignKey('states.state_id'), index=True)
    # session_id = Column(ForeignKey('sessions.session_id'), index=True)
    # static_member_id = Column(ForeignKey('members_aggregate.member_id'), index=True)
    chamber = Column(String(5))
    party = Column(String(100))
    district = Column(String(100))
    seat_id = Column(String(10))
    county = Column(String(100))
    committees = Column(String(300))
    leadership_positions = Column(String(100))
    partial_session = Column(TINYINT)
    early_end_date = Column(Date)
    notes = Column(String(200))
    city_of_residence = Column(String(100))
    elected_appointed_date = Column(Date)
    path_to_office = Column(TINYINT)

    # session = relationship('Session')
    # state1 = relationship('State')
    # static_member = relationship('MembersAggregate')

class MembersBySessionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MembersBySession
        load_instance = True

class BillHistory(db.Model):
    __tablename__ = 'bill_history'

    action_id = Column(String(25), primary_key=True)
    # bill_id = Column(ForeignKey('bills.bill_id'), index=True)
    bill_id = Column(String(100))
    action = Column(String)
    action_category = Column(String)
    chamber = Column(String(5))
    date = Column(Date)
    # committee_id = Column(ForeignKey('committees.committee_id'), index=True)
    committee_id =  Column(String(15))
    outcome = Column(String)

    # bill = relationship('Bill')
    # committee = relationship('Committee')

class BillHistorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BillHistory
        load_instance = True

# # t_committee_membership = Table(
# #     'committee_membership', metadata,
# #     Column('committee_id', ForeignKey('committees.committee_id'), index=True),
# #     Column('static_member_id', ForeignKey('members_aggregate.member_id'), index=True),
# #     Column('member_session_id', ForeignKey('members_by_session.member_session_id'), index=True)
# # )


class Sponsor(db.Model):
    __tablename__ = 'sponsors'

    sponsor_id = Column(String(25), primary_key=True)
    # bill_id = Column(ForeignKey('bills.bill_id'), index=True)
    # member_session_id = Column(ForeignKey('members_by_session.member_session_id'), index=True)
    bill_id = Column(String(100))
    member_session_id = Column(String(20))
    state_sponsor_type = Column(String(100))
    hsp_sponsor_type = Column(String(100))

#     bill = relationship('Bill')
#     member_session = relationship('MembersBySession')

class SponsorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Sponsor
        load_instance = True

class FloorVote(db.Model):
    __tablename__ = 'floor_vote'

    floor_vote_id = Column(Integer, primary_key=True)
    vote = Column(String(20))
    bill_id = Column(String(100))
    member_session_id = Column(String(20))
    action_id = Column(String(25))
    # member_session_id = Column(ForeignKey('members_by_session.member_session_id'), index=True)
    # bill_id = Column(ForeignKey('bills.bill_id'), index=True)
    # action_id = Column(ForeignKey('bill_history.action_id'), index=True)

class FloorVoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = FloorVote
        load_instance = True
