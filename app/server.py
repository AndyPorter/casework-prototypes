import os
import json

from flask import Flask, render_template
from flask.ext.assets import Environment

app = Flask(__name__)
app.debug = True

# govuk_template asset path
@app.context_processor
def asset_path_context_processor():
  return {
    'asset_path': '/static/govuk-template/',
    'prototypes_asset_path': '/static/'
  }

@app.route('/')
def home():
  return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('common/proto-404.html'), 404

@app.route('/404')
def edge_of_proto(e):
    return render_template('common/proto-404.html')

@app.route('/proto')
def proto():
  return render_template('index2.html')

@app.route('/hack-day')
def hackday():
  return render_template('index-hack.html')

# ---------------------------------------------------------------------------

#hackday 
@app.route('/hackday/land-ownership-record')
def hackday_land_record():
  return render_template('hackday/land-record.html', next_page="404")

@app.route('/hackday/land-ownership-record-1')
def hackday_land_record_1():
  return render_template('hackday/land-record-1.html', next_page="404")

@app.route('/hackday/land-ownership-record-2')
def hackday_land_record_2():
  return render_template('hackday/land-record-2.html', next_page="404")

# ---------------------------------------------------------------------------

# LAST OF THE ALPHA PROTOTYPES!

# A "citizen facing" register concept
#
# If we're having to download a "legal copy" then this page can be much more straightforward
@app.route('/register-view/register-view-citizen-1')
def register_view_citizen_1():
  return render_template('register-view/register-view-citizen-1.html', next_page="404")

# ---------------------------------------------------------------------------

#  -----------------
@app.route('/common/payment')
def common_payment():
  return render_template('common/payment.html', next_page="/")

# ---------------------------------------------------------------------------

# GOV.UK pages, search / start v2.0 -----------------
@app.route('/govuk/search-2.0')
def govuk_search_2_0():
  return render_template('govuk-views/search-2.0.html')

# GOV.UK pages, results listing v2.0 -----------------
@app.route('/govuk/results-2.0')
def govuk_results_2_0():
  return render_template('govuk-views/results-2.0.html')

# GOV.UK pages, property details v2.0 -----------------
@app.route('/govuk/property-details-2.0')
def govuk_property_details_2_0():
  return render_template('govuk-views/property-details-2.0.html')

# GOV.UK pages, property details v2.1 -----------------
@app.route('/govuk/property-details-2.1')
def govuk_property_details_2_1():
  return render_template('govuk-views/property-details-2.1.html')


# ---------------------------------------------------------------------------

# scenario: user wants to find out who owns a property
# starts on GOV.UK and flows into register view 
@app.route('/find-owner/search')
def find_owner_search():
  return render_template('user-find-owner/search.html', next_page="/find-owner/results")

# GOV.UK pages, results listing -----------------
@app.route('/find-owner/results')
def find_owner_results():
  return render_template('user-find-owner/results.html', next_page="/find-owner/property-details-2.0")

# GOV.UK pages, property details v2.0 -----------------
@app.route('/find-owner/property-details-2.0')
def find_owner_details_2_0():
  return render_template('user-find-owner/property-details-2.0.html', next_page="/find-owner/verify")

# GOV.UK pages, IDA/Credit Card/login stuff -----------------

# Step 1 - login with GOV.UK Verify - use sub flow...

#       Sub flow - GOV.UK Verification ---------------------

# GOV.UK verify - Sub flow Step 1 - for conveyancer create relationship flow
@app.route('/find-owner/verify')
def find_owner_verify():
  return render_template('user-find-owner/govuk-verify/verify-intro.html', next_page="/find-owner/who-verified-you")

# GOV.UK verify -  Sub flow Step 2 - who verified you
@app.route('/find-owner/who-verified-you')
def find_owner_verify_who():
  return render_template('user-find-owner/govuk-verify/verify-who.html', next_page="/find-owner/experian-sign-in")

# GOV.UK verify - Sub flow Step 3 - experian sign in
@app.route('/find-owner/experian-sign-in')
def find_owner_verify_experian_sign_in_1():
  return render_template('user-find-owner/govuk-verify/verify-sign-in.html', next_page="/find-owner/experian-sign-in-part-2")

# GOV.UK verify - Sub flow Step 4 - experian 2nd phase sign in
@app.route('/find-owner/experian-sign-in-part-2')
def find_owner_verify_experian_sign_in_2nd_part_1():
  return render_template('user-find-owner/govuk-verify/verify-sign-in-2.html', next_page="/find-owner/register-view")

#       end Sub flow - GOV.UK Verification ---------------------

# GOV.UK pages, property details v2.0 -----------------
@app.route('/find-owner/register-view')
def find_owner_register_view():
  return render_template('user-find-owner/register-3.0.html', next_page="/find-owner/changes-view")

# GOV.UK pages, property details v2.0 -----------------
@app.route('/find-owner/changes-view')
def find_owner_historian_view():
  return render_template('user-find-owner/changes-1.0.html', next_page="/")

# ---------------------------------------------------------------------------

# scenario: user wants to find out who owns a property (IDA + payment)
# starts on GOV.UK and flows into register view
@app.route('/find-owner/b/search')
def find_owner_b_search():
  return render_template('user-find-owner/search.html', next_page="/find-owner/b/results")

# GOV.UK pages, results listing -----------------
@app.route('/find-owner/b/results')
def find_owner_b_results():
  return render_template('user-find-owner/results.html', next_page="/find-owner/b/property-details-2.0")

# GOV.UK pages, property details v2.0 -----------------
@app.route('/find-owner/b/property-details-2.0')
def find_owner_b_details_2_0():
  return render_template('user-find-owner/property-details-2.1.html', next_page="/find-owner/b/verify")

# Sub flow - GOV.UK Verification ---------------------

# GOV.UK verify - Sub flow Step 1
@app.route('/find-owner/b/verify')
def find_owner_b_verify():
  return render_template('user-find-owner/govuk-verify/verify-intro.html', next_page="/find-owner/b/who-verified-you")

# GOV.UK verify -  Sub flow Step 2
@app.route('/find-owner/b/who-verified-you')
def find_owner_b_verify_who():
  return render_template('user-find-owner/govuk-verify/verify-who.html', next_page="/find-owner/b/experian-sign-in")

# GOV.UK verify - Sub flow Step 3 - experian sign in
@app.route('/find-owner/b/experian-sign-in')
def find_owner_b_verify_experian_sign_in_1():
  return render_template('user-find-owner/govuk-verify/verify-sign-in.html', next_page="/find-owner/b/experian-sign-in-part-2")

# GOV.UK verify - Sub flow Step 4 - experian 2nd phase sign in
@app.route('/find-owner/b/experian-sign-in-part-2')
def find_owner_b_verify_experian_sign_in_2nd_part_1():
  return render_template('user-find-owner/govuk-verify/verify-sign-in-2.html', next_page="/find-owner/b/card-payment")

# end Sub flow - GOV.UK Verification ---------------------

# Sub flow - card payment ---------------------

# GOV.UK pages, accept cost to view register -----------------
@app.route('/find-owner/b/accept-cost')
def find_owner_b_accept_cost():
  return render_template('user-find-owner/accept-cost.html', next_page="/find-owner/b/card-payment")

# GOV.UK pages, pay to view register -----------------
@app.route('/find-owner/b/card-payment')
def find_owner_b_card_payment():
  return render_template('common/payment.html', next_page="/find-owner/register-view")

# end sub flow - card payment ---------------------

# ---------------------------------------------------------------------------

# scenario: user wants to find out who owns a property rouute c - (IDA) (real fake title)
# starts on GOV.UK and flows into register view
@app.route('/find-owner/c/search')
def find_owner_c_search():
  return render_template('user-find-owner/search.html', next_page="/find-owner/c/results")

# GOV.UK pages, results listing -----------------
@app.route('/find-owner/c/results')
def find_owner_c_results():
  return render_template('user-find-owner/results-c.html', next_page="/find-owner/c/property-details-2.0")

# GOV.UK pages, property details v2.0 -----------------
@app.route('/find-owner/c/property-details-2.0')
def find_owner_c_details_2_0():
  return render_template('user-find-owner/property-details-2.1-c.html', next_page="/find-owner/c/verify")

# Sub flow - GOV.UK Verification ---------------------

# GOV.UK verify - Sub flow Step 1
@app.route('/find-owner/c/verify')
def find_owner_c_verify():
  return render_template('user-find-owner/govuk-verify/verify-intro.html', next_page="/find-owner/c/who-verified-you")

# GOV.UK verify -  Sub flow Step 2
@app.route('/find-owner/c/who-verified-you')
def find_owner_c_verify_who():
  return render_template('user-find-owner/govuk-verify/verify-who.html', next_page="/find-owner/c/experian-sign-in")

# GOV.UK verify - Sub flow Step 3 - experian sign in
@app.route('/find-owner/c/experian-sign-in')
def find_owner_c_verify_experian_sign_in_1():
  return render_template('user-find-owner/govuk-verify/verify-sign-in.html', next_page="/find-owner/c/experian-sign-in-part-2")

# GOV.UK verify - Sub flow Step 4 - experian 2nd phase sign in
@app.route('/find-owner/c/experian-sign-in-part-2')
def find_owner_c_verify_experian_sign_in_2nd_part_1():
  return render_template('user-find-owner/govuk-verify/verify-sign-in-2.html', next_page="/find-owner/c/register-view")

# end Sub flow - GOV.UK Verification ---------------------

# GOV.UK pages, property details v2.0 -----------------
@app.route('/find-owner/c/register-view')
def find_owner_c_register_view():
  return render_template('register-view/register-test-title.html')

# ---------------------------------------------------------------------------


# scenario: user wants to find out ... something about a property
# starts on GOV.UK and flows into register view
# Verify + Payment + real fake title
@app.route('/find-owner/d/search')
def find_owner_d_search():
  return render_template('user-find-owner/search.html', next_page="/find-owner/d/results")

# GOV.UK pages, results listing -----------------
@app.route('/find-owner/d/results')
def find_owner_d_results():
  return render_template('user-find-owner/results-c.html', next_page="/find-owner/d/property-details-2.0")

# GOV.UK pages, property details v2.0 -----------------
@app.route('/find-owner/d/property-details-2.0')
def find_owner_d_details_2_0():
  return render_template('user-find-owner/property-details-2.1-c.html', next_page="/find-owner/d/verify")

#   Verify ---------------------

# verify - Step 1
@app.route('/find-owner/d/verify')
def find_owner_d_verify():
  return render_template('user-find-owner/govuk-verify/verify-intro.html', next_page="/find-owner/d/who-verified-you")

# verify - Step 2
@app.route('/find-owner/d/who-verified-you')
def find_owner_d_verify_who():
  return render_template('user-find-owner/govuk-verify/verify-who.html', next_page="/find-owner/d/experian-sign-in")

# verify - Step 3 - experian sign in
@app.route('/find-owner/d/experian-sign-in')
def find_owner_d_verify_experian_sign_in_1():
  return render_template('user-find-owner/govuk-verify/verify-sign-in.html', next_page="/find-owner/d/experian-sign-in-part-2")

# verify - Step 4 - experian 2nd phase sign in
@app.route('/find-owner/d/experian-sign-in-part-2')
def find_owner_d_verify_experian_sign_in_2nd_part_1():
  return render_template('user-find-owner/govuk-verify/verify-sign-in-2.html', next_page="/find-owner/d/card-payment")

#   end Verify ---------------------

#   card payment ---------------------

# pay to view register -----------------
@app.route('/find-owner/d/card-payment')
def find_owner_d_card_payment():
  return render_template('common/payment.html', next_page="/find-owner/d/register-view")

# end card payment ---------------------

# GOV.UK pages, property details v2.0 -----------------
@app.route('/find-owner/d/register-view')
def find_owner_d_register_view():
  return render_template('register-view/register-test-title.html')

# ---------------------------------------------------------------------------

# Alternate Register view.  V4 with sections fully open

@app.route('/register-view/register-view-4-expanded')
def register_view_4_0_expanded():
  return render_template('register-view/register-test-title-expanded.html', next_page="404")

# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------

# Alternate Register view.  V4 with help on show

@app.route('/register-view/register-view-4-help-text')
def register_view_4_0_help_text():
  return render_template('register-view/register-test-title-help.html', next_page="404")

# ---------------------------------------------------------------------------

# Transfer prototypes, login page
@app.route('/transfer/login')
def transfer_login():
  return render_template('common/login.html', next_page="/transfer/conveyancer-case-list")

# Transfer prototypes, conveyancer-case-list page
@app.route('/transfer/conveyancer-case-list')
def conveyancer_case_list():
  json_data=open('app/static/data/cases.json', "r")
  data = json.load(json_data)
  return render_template('transfer/conveyancer-case-list.html', data=data)

# Transfer prototypes, create transfer page
@app.route('/transfer/create-transfer')
def create_transfer():
  json_data=open('app/static/data/complete-transfer.json', "r")
  data = json.load(json_data)
  return render_template('transfer/create-transfer.html', editable=True, data=data)

# Transfer prototypes, new provisions page
@app.route('/transfer/new-provisions')
def transfer_new_provisions():
  return render_template('transfer/new-provisions.html')

# Transfer prototypes, mortgage details page
@app.route('/transfer/mortgage-details')
def transfer_mortgage_details():
  return render_template('transfer/mortgage-details.html')

# Transfer prototypes, mortgage details entered page
@app.route('/transfer/mortgage-details-entered')
def transfer_mortgage_details_entered():
  return render_template('transfer/mortgage-details-entered.html')

# Transfer prototypes, summary page
@app.route('/transfer/summary')
def transfer_summary():
  json_data=open('app/static/data/complete-transfer.json', "r")
  data = json.load(json_data)
  return render_template('transfer/summary.html', editable=True, conveyancer="buyer", data=data)

# Transfer prototypes, summary with no mortgage details page
@app.route('/transfer/summary-no-mortgage')
def transfer_summary_no_mortgage():
  json_data=open('app/static/data/no-mortgage.json', "r")
  data = json.load(json_data)
  return render_template('transfer/summary-no-mortgage.html', editable=True, conveyancer="buyer", data=data)

# Transfer prototypes, transfer that has been withdrawn
@app.route('/transfer/transfer-withdrawn')
def transfer_withdrawn():
  json_data=open('app/static/data/withdrawn-transfer.json', "r")
  data = json.load(json_data)
  return render_template('transfer/transfer-withdrawn.html', editable=True, data=data)

# Transfer prototypes, summary with option to withdraw
@app.route('/transfer/summary-withdraw-option')
def transfer_withdraw_option():
  json_data=open('app/static/data/complete-transfer.json', "r")
  data = json.load(json_data)
  return render_template('transfer/summary-withdraw-option.html', editable=False, data=data)

# Transfer prototypes, summary with empty states
@app.route('/transfer/transfer-empty-states')
def transfer_empty_states():
  json_data=open('app/static/data/incomplete-transfer.json', "r")
  data = json.load(json_data)
  return render_template('transfer/transfer-empty-states.html', editable=True, data=data)

# Transfer prototypes, done page
@app.route('/transfer/done')
def transfer_done():
  return render_template('transfer/done.html')

# Transfer prototypes, signing the transfer page
@app.route('/transfer/transfer-signing')
def transfer_signing():
  json_data=open('app/static/data/ready-to-sign-transfer.json', "r")
  data = json.load(json_data)
  return render_template('transfer/transfer-signing.html', editable=False, data=data, role="buyer")

# Transfer prototypes, signing the transfer page
@app.route('/transfer/transfer-signing-seller')
def transfer_signing_seller():
  json_data=open('app/static/data/ready-to-sign-transfer.json', "r")
  data = json.load(json_data)
  return render_template('transfer/transfer-signing-seller.html', editable=False, data=data, role="seller")

# ---------------------------------------------------------------------------

# Transfer prototypes - 2nd conveyancer, Step 1 - login page
@app.route('/transfer-2nd-con/login')
def transfer_2nd_conveyancer_login():
  return render_template('common/login.html', next_page="/transfer-2nd-con/conveyancer-case-list")

# Transfer prototypes - 2nd conveyancer, Step 2 - conveyancer-case-list
@app.route('/transfer-2nd-con/conveyancer-case-list')
def transfer_2nd_conveyancer_case_list():
  json_data=open('app/static/data/cases-seller.json', "r")
  data = json.load(json_data)
  return render_template('transfer-2nd-conveyancer/conveyancer-case-list.html', data=data)

# Transfer prototypes - 2nd conveyancer, Step 3 - confirm page
@app.route('/transfer-2nd-con/review-transfer')
def transfer_2nd_conveyancer_review_transfer():
  json_data=open('app/static/data/complete-transfer.json', "r")
  data = json.load(json_data)
  return render_template('transfer-2nd-conveyancer/review-transfer.html', editable=False, data=data, role="seller")

# Transfer prototypes - 2nd conveyancer, Step 4 - transfer ready to sign
@app.route('/transfer-2nd-con/marked-ready')
def transfer_2nd_conveyancer_marked_ready():
  return render_template('transfer-2nd-conveyancer/marked-ready.html')

# Transfer prototypes, transfer that has been withdrawn
@app.route('/transfer-2nd-con/transfer-withdrawn')
def transfer_2nd_con_withdrawn():
  json_data=open('app/static/data/withdrawn-transfer.json', "r")
  data = json.load(json_data)
  return render_template('transfer/transfer-withdrawn.html', editable=False, data=data)

# ---------------------------------------------------------------------------

# Transaction flows, citizens sign transfer and charge v2.0 -----------------
@app.route('/transfer-and-charge/citizen-1-start')
def transfer_and_charge_citizen_1_start_2_0():
  return render_template('transfer-and-charge/citizen-1-start-2.0.html', next_page="citizen-1-login")

# Step 1 - login with GOV.UK Verify
@app.route('/transfer-and-charge/citizen-1-login')
def transfer_and_charge_citizen_1_login_2_0():
  return render_template('transfer-and-charge/citizen-1-login-2.0.html', next_page="citizen-1-enter-token")

# Step 2 - Client 1 enters token
@app.route('/transfer-and-charge/citizen-1-enter-token')
def transfer_and_charge_citizen_1_enter_token_2_0():
  return render_template('transfer-and-charge/citizen-1-enter-token-2.0.html', next_page="citizen-1-sign-mortgage")

# Step 3 - Client 1 signs mortgage deed
@app.route('/transfer-and-charge/citizen-1-sign-mortgage')
def transfer_and_charge_citizen_1_sign_mortgage_2_0():
  return render_template('transfer-and-charge/citizen-1-sign-mortgage-2.0.html', next_page="citizen-1-sign-transfer")

# Step 4 - Client 1 signs transfer
@app.route('/transfer-and-charge/citizen-1-sign-transfer')
def transfer_and_charge_citizen_1_sign_transfer_2_0():
  return render_template('transfer-and-charge/citizen-1-sign-transfer-2.0.html', next_page="citizen-1-semi-confirmed")

# Step 5 - Client 1 - semi confirmation
@app.route('/transfer-and-charge/citizen-1-semi-confirmed')
def transfer_and_charge_citizen_1_semi_confirmed_2_0():
  return render_template('transfer-and-charge/citizen-1-semi-confirmed-2.0.html')

# ---------------------------------------------------------------------------

# Transaction flows, citizens sign transfer and charge v3 -----------------

# Step 1a - external process step - show user email
@app.route('/transfer-and-charge-v3/citizen-1-email')
def transfer_and_charge_citizen_1_email_3_0():
  return render_template('transfer-and-charge/citizen-1-email-2.0.html', next_page="citizen-1-start")

@app.route('/transfer-and-charge-v3/citizen-1-start')
def transfer_and_charge_citizen_1_start_3_0():
  return render_template('transfer-and-charge/citizen-1-start-2.0.html', next_page="citizen-1-login")

# Step 1 - login with GOV.UK Verify
@app.route('/transfer-and-charge-v3/citizen-1-login')
def transfer_and_charge_citizen_1_login_3_0():
  return render_template('transfer-and-charge/citizen-1-login-2.0.html', next_page="citizen-1-enter-token")


# Step 2 - Client 1 enters token
@app.route('/transfer-and-charge-v3/citizen-1-enter-token')
def transfer_and_charge_citizen_1_enter_token_3_0():
  return render_template('transfer-and-charge/citizen-1-enter-token-2.0.html', next_page="citizen-1-sign-mortgage")

# Step 3 - Client 1 signs mortgage deed
@app.route('/transfer-and-charge-v3/citizen-1-sign-mortgage')
def transfer_and_charge_citizen_1_sign_mortgage_3_0():
  return render_template('transfer-and-charge/citizen-1-sign-mortgage-2.0.html', next_page="/transfer-and-charge-v3/citizen-1-sign-transfer")

# Step 3 - Client 1 signs transfer deed
@app.route('/transfer-and-charge-v3/citizen-1-sign-transfer')
def transfer_and_charge_citizen_1_sign_transfer_3_0():
  json_data=open('app/static/data/transfer-signing-data.json', "r")
  data = json.load(json_data)
  return render_template('transfer/transfer-signing.html', next_page="/transfer-and-charge-v3/citizen-1-sms", data=data, role="citizen")

# Step 3a - external process step - show user sms message
@app.route('/transfer-and-charge-v3/citizen-1-sms')
def transfer_and_charge_citizen_1_sms_3_0():
  return render_template('transfer-and-charge/citizen-1-sms-2.0.html', next_page="citizen-1-2-factor-auth")

# Step 4 - Client 1 2 factor authentication
@app.route('/transfer-and-charge-v3/citizen-1-2-factor-auth')
def transfer_and_charge_citizen_1_2_factor_auth():
  return render_template('transfer-and-charge/citizen-1-2-factor.html', next_page="/transfer-and-charge-v3/citizen-1-semi-confirmed")

# Step 5 - Client 1 - semi confirmation
@app.route('/transfer-and-charge-v3/citizen-1-semi-confirmed')
def transfer_and_charge_citizen_1_semi_confirmed_3_0():
  return render_template('transfer-and-charge/citizen-1-semi-confirmed-2.0.html')

# ---------------------------------------------------------------------------

# Transaction flows, relationship starts, conveyancer initiates v2.2 --------
@app.route('/relationship-starts/conveyancer-start')
def conveyancer_start_2_2():
  return render_template('relationship-starts/conveyancer-start-2.2.html')

# Step 1 - log in
@app.route('/relationship-starts/login')
def relationship_starts_login_2_2():
  return render_template('common/login.html', next_page="/relationship-starts/conveyancer-find-property")

# Step 2 - find correct property
@app.route('/relationship-starts/conveyancer-find-property')
def conveyancer_find_property_2_2():
  return render_template('relationship-starts/conveyancer-find-property-2.2.html')

# Step 3 - results and select correct property
@app.route('/relationship-starts/conveyancer-select-property')
def conveyancer_select_property_2_2():
  return render_template('relationship-starts/conveyancer-select-property-2.2.html')

# Step 4 - select associated task
@app.route('/relationship-starts/conveyancer-select-task')
def conveyancer_select_task_2_2():
  return render_template('relationship-starts/conveyancer-select-task-2.2.html')

# Step 5 - set the number of clients
@app.route('/relationship-starts/conveyancer-add-clients')
def conveyancer_add_clients_2_2():
  return render_template('relationship-starts/conveyancer-add-clients-2.2.html')

# Step 6 - add 1st client
@app.route('/relationship-starts/conveyancer-add-client-1')
def conveyancer_add_client_1_2_2():
  return render_template('relationship-starts/conveyancer-add-client-1-2.2.html')

# Step 7 - add 2nd client
@app.route('/relationship-starts/conveyancer-add-client-2')
def conveyancer_add_client_2_2_2():
  return render_template('relationship-starts/conveyancer-add-client-2-2.2.html')

# Step 8 - confirmation
@app.route('/relationship-starts/conveyancer-confirm')
def conveyancer_confirm_2_2():
  return render_template('relationship-starts/conveyancer-confirm-2.2.html')

# Step 9 - generated token
@app.route('/relationship-starts/conveyancer-token')
def conveyancer_token_2_2():
  return render_template('relationship-starts/conveyancer-token-2.2.html')

# ---------------------------------------------------------------------------

# Transaction flows, relationship starts, client(s) confirm v2.2 --------
@app.route('/relationship-starts/client-start')
def client_start_2_2():
  return render_template('relationship-starts/client-start-2.2.html')

# Step 1 - login with GOV.UK Verify - use sub flow...

#       Sub flow - GOV.UK Verification ---------------------

# GOV.UK verify - Sub flow Step 1 - for conveyancer create relationship flow
@app.route('/relationship-starts/client-login')
def client_verify_2_2():
  return render_template('relationship-starts/verify-subflow-client-1/verify-intro.html')

# GOV.UK verify -  Sub flow Step 2 - who verified you
@app.route('/relationship-starts/client-who-verified-you')
def relationship_starts_client_verify_who_1():
  return render_template('relationship-starts/verify-subflow-client-1/verify-who.html')

# GOV.UK verify - Sub flow Step 3 - experian sign in
@app.route('/relationship-starts/client-experian-sign-in')
def relationship_starts_client_verify_experian_sign_in_1():
  return render_template('relationship-starts/verify-subflow-client-1/verify-sign-in.html')

# GOV.UK verify - Sub flow Step 4 - experian 2nd phase sign in
@app.route('/relationship-starts/client-experian-sign-in-part-2')
def relationship_starts_client_verify_experian_sign_in_2nd_part_1():
  return render_template('relationship-starts/verify-subflow-client-1/verify-sign-in-2.html')

#       end Sub flow - GOV.UK Verification ---------------------

# Step 2 - Client 1 enters token
@app.route('/relationship-starts/client-enter-token')
def client_enter_token_2_1():
  return render_template('relationship-starts/client-enter-token-2.1.html')

# Step 3 - Client 1 confirms
@app.route('/relationship-starts/client-confirm')
def client_confirm_2_2():
  return render_template('relationship-starts/client-confirm-2.2.html')

# Step 4 - Client 1 receives confirmation
@app.route('/relationship-starts/client-semi-confirmed')
def client_semi_confirmed_2_2():
  return render_template('relationship-starts/client-semi-confirmed-2.2.html')

# Step 5 - Client can now view the register if they want to.
@app.route('/relationship-starts/client-view-register')
def client_view_register_2_1():
  return render_template('relationship-starts/register-2.1-no-pending.html')

# Step 6 - Client 2 visits start page
@app.route('/relationship-starts/client-2-start')
def client_2_start_2_2():
  return render_template('relationship-starts/client-2-start-2.2.html')

# Step 7 - login with GOV.UK Verify - use sub flow...

#       Sub flow - GOV.UK Verification ---------------------

# GOV.UK verify - Sub flow Step 1 - for conveyancer create relationship flow
@app.route('/relationship-starts/client-2-login')
def client_2_verify_2_0():
  return render_template('relationship-starts/verify-subflow-client-2/verify-intro.html')

# GOV.UK verify -  Sub flow Step 2 - who verified you
@app.route('/relationship-starts/client-2-who-verified-you')
def relationship_starts_client_2_verify_who_1():
  return render_template('relationship-starts/verify-subflow-client-2/verify-who.html')

# GOV.UK verify - Sub flow Step 3 - experian sign in
@app.route('/relationship-starts/client-2-experian-sign-in')
def relationship_starts_client_2_verify_experian_sign_in_1():
  return render_template('relationship-starts/verify-subflow-client-2/verify-sign-in.html')

# GOV.UK verify - Sub flow Step 4 - experian 2nd phase sign in
@app.route('/relationship-starts/client-2-experian-sign-in-part-2')
def relationship_starts_client_2_verify_experian_sign_in_2nd_part_1():
  return render_template('relationship-starts/verify-subflow-client-2/verify-sign-in-2.html')

#       end Sub flow - GOV.UK Verification ---------------------

# Step 8 - Client 2 enters token
@app.route('/relationship-starts/client-2-enter-token')
def client_2_enter_token_2_0():
  return render_template('relationship-starts/client-2-enter-token-2.0.html')

# Step 9 - Client 2 confirms
@app.route('/relationship-starts/client-2-confirm')
def client_2_confirm_2_2():
  return render_template('relationship-starts/client-2-confirm-2.2.html')

# Step 10 - Client 2 receives (all parties) confirmation
@app.route('/relationship-starts/clients-confirmed')
def clients_confirmed_2_2():
  return render_template('relationship-starts/clients-confirmed-2.2.html')

# ---------------------------------------------------------------------------

# Transaction flows, relationship starts, citizen confirms v2.0 --------
@app.route('/relationship-starts/citizen-confirms')
def citizen_confirms_2_0():
  return render_template('relationship-starts/citizen-confirms-2.0.html')

# ---------------------------------------------------------------------------

# Page prototypes, Register View --------------------------
@app.route('/register-view/register-2.0')
def register_2_0():
  return render_template('register-view/register-2.0.html')
@app.route('/register-view/register-2.1')
def register_2_1():
  return render_template('register-view/register-2.1.html')
@app.route('/register-view/register-3.0')
def register_3_0():
  return render_template('register-view/register-3.0.html')
@app.route('/register-view/register-test-title')
def register_test_title():
  return render_template('register-view/register-test-title.html')
@app.route('/register-view/register-hybrid')
def register_hybrid():
  return render_template('register-view/register-hybrid.html')


# ---------------------------------------------------------------------------

# Page prototypes, Register Changes View --------------------------

# Change history - pending and historical
@app.route('/changes-view/changes-1.0')
def changes_1_0():
  return render_template('changes-view/changes-1.0.html')

# Change history - historical only - nothing pending
@app.route('/changes-view/changes-no-pending-1.0')
def changes_no_pending_1_0():
  return render_template('changes-view/changes-no-pending-1.0.html')

# ---------------------------------------------------------------------------

# Page prototypes, Example mortgage agreement  --------------------------
@app.route('/legal-documents/mortgage-agreement-v1')
def mortgage_agreement_1():
  return render_template('legal-documents/mortgage-agreement-v1.html')

# Page prototypes, Example transfer agreement  --------------------------
@app.route('/legal-documents/transfer-agreement-v1')
def transfer_agreement_1():
  return render_template('legal-documents/transfer-agreement-v1.html')

# ---------------------------------------------------------------------------

# Reserve Priority (Freeze register)  ---------------------------------------
@app.route('/reserve-priority/select')
def reserve_priority_1_select():
  return render_template('reserve-priority/protect-what-2.0.html')

@app.route('/reserve-priority/confirm')
def reserve_priority_2_confirm():
  return render_template('reserve-priority/protect-confirm-2.0.html')

@app.route('/reserve-priority/confirmed')
def reserve_priority_3_confirmed():
  return render_template('reserve-priority/protect-confirmed-2.0.html')

# ---------------------------------------------------------------------------

# Sprint 4, Relationship verifier flow --------------------------
@app.route('/sprint-4/citizen-reference')
def sprint_4_reference():
  return render_template('sprint-4/relationship/citizen-reference.html')

@app.route('/sprint-4/citizen-login')
def sprint_4_citizen_login():
  return render_template('sprint-4/relationship/citizen-login.html')

@app.route('/sprint-4/citizen-confirm')
def sprint_4_citizen_confirm():
  return render_template('sprint-4/relationship/citizen-confirm.html')

@app.route('/sprint-4/citizen-complete')
def sprint_4_citizen_complete():
  return render_template('sprint-4/relationship/citizen-complete.html')

@app.route('/sprint-4/citizen-register')
def sprint_4_citizen_register():
  return render_template('sprint-4/relationship/citizen-register.html')

# ---------------------------------------------------------------------------

# Sprint 3, Register view --------------------------
@app.route('/sprint-3/register-v1')
def sprint_3_register_v1():
  return render_template('sprint-3/register-view/register-v1.html')

@app.route('/sprint-3/register-v1a-history')
def sprint_3_register_v1a_history():
  return render_template('sprint-3/register-view/register-v1a-history.html')

@app.route('/sprint-3/register-v1a-history-1')
def sprint_3_register_v1a_history_1():
  return render_template('sprint-3/register-view/register-v1a-history-1.html')

# Sprint 3, prototype 1, conveyancer - buyer relationship --------------------------
@app.route('/sprint-3/conveyancer-start')
def sprint_3_conveyancer_start():
  return render_template('sprint-3/buyer-conveyancer/conveyancer-0-start.html')

@app.route('/sprint-3/conveyancer-login')
def sprint_3_conveyancer_login():
  return render_template('sprint-3/buyer-conveyancer/conveyancer-1-login.html')

@app.route('/sprint-3/conveyancer-enter-title')
def sprint_3_conveyancer_enter_title():
  return render_template('sprint-3/buyer-conveyancer/conveyancer-2-enter-title.html')

@app.route('/sprint-3/conveyancer-add-buyers')
def sprint_3_conveyancer_add_buyers():
  return render_template('sprint-3/buyer-conveyancer/conveyancer-5-add-buyers.html')

@app.route('/sprint-3/relationship-reference')
def sprint_3_relationship_reference():
  return render_template('sprint-3/buyer-conveyancer/conveyancer-6-ref-for-buyers.html')

# Sprint 3, prototype 1, buyer -> conveyancer relationship --------------------------
@app.route('/sprint-3/buyer-login')
def sprint_3_buyer_login():
  return render_template('sprint-3/buyer-conveyancer/buyer-1-login.html')

@app.route('/sprint-3/buyer-ref-code')
def sprint_3_buyer_ref_code():
  return render_template('sprint-3/buyer-conveyancer/buyer-2-reference-code.html')

@app.route('/sprint-3/buyer-register')
def sprint_3_buyer_register():
  return render_template('sprint-3/buyer-conveyancer/buyer-3-register.html')


# Sprint 3, Execute Deed - reworked from sprint 2 -----------------------------------
@app.route('/sprint-3/buyer-signing-start')
def sprint_3_buyer_signing_start():
  return render_template('sprint-3/deed/buyer-0-start.html')

@app.route('/sprint-3/buyer-signing-login')
def sprint_3_buyer_signing_login():
  return render_template('sprint-3/deed/buyer-0a-login.html')

@app.route('/sprint-3/display-charge-for-signing')
def sprint_3_execute_deed():
  return render_template('sprint-3/deed/buyer-1-sign-charge.html')

@app.route('/sprint-3/display-transfer-for-signing')
def sprint_3_execute_transfer():
  return render_template('sprint-3/deed/buyer-1a-sign-transfer.html')


@app.route('/sprint-3/two-factor')
def sprint_3_two_factor():
  return render_template('sprint-3/deed/buyer-2-two-factor.html')

@app.route('/sprint-3/signing-complete')
def sprint_3_signing_complete():
  return render_template('sprint-3/deed/buyer-3-signing-complete.html')

# ---------------------------------------------------------------------------

# Sprint 2, prototype 1: Passing a "token" -----------------------------------------
@app.route('/sprint-2/token')
def sprint_2_token():
  return render_template('sprint-2/token/citizen-1-register.html')

@app.route('/sprint-2/select-action')
def sprint_2_select_action():
  return render_template('sprint-2/token/citizen-2-select-action.html')

@app.route('/sprint-2/choose-method')
def sprint_2_choose_method():
  return render_template('sprint-2/token/citizen-3-choose-method.html')

@app.route('/sprint-2/generate-token')
def sprint_2_generate_token():
  return render_template('sprint-2/token/citizen-4-generate-token.html')

@app.route('/sprint-2/show-change')
def sprint_2_show_change():
  return render_template('sprint-2/token/citizen-5-register-during-change.html')

@app.route('/sprint-2/input-token')
def sprint_2_input_token():
  return render_template('sprint-2/token/conveyancer-1-input-token.html')

@app.route('/sprint-2/retrieve-token')
def sprint_2_retrieve_token():
  return render_template('sprint-2/token/conveyancer-2-retrieve-details.html')

# Sprint 2, spike - Execute Deed -----------------------------------------
@app.route('/sprint-2/execute-deed')
def sprint_2_execute_deed():
  return render_template('sprint-2/deed/buyer-1-execute-deed.html')

@app.route('/sprint-2/execution-complete')
def sprint_2_execution_complete():
  return render_template('sprint-2/deed/buyer-2-execution-complete.html')


# Example pages - for designers -----------------------------------------
@app.route('/examples/example-1')
def example_1():
  return render_template('examples/example-page.html')



if __name__ == '__main__':
  # Bind to PORT if defined, otherwise default to 5000.
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
