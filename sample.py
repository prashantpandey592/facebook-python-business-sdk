# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.customaudience import CustomAudience
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adpreview import AdPreview
from facebook_business.api import FacebookAdsApi

access_token = 'EAAFBk76SFuUBAJEFGP7vvsMwCD0gorceiCfC89UQd23qyZCcy6MGnjCSlpWiGknshWfcaYcgsoFaaK7ui6ZB5zJBicZChskuUZCAyJpmKnbGbB7zxC8WYrjX7cE6xV1oL2VHbD1ZBeAfav7X8SMBvQlbIVBH1JhQk43dQRA9wzxZCtXBoMGtTzDnh8gJgG6VwZD'
app_secret = 'e982b19e36b1d61bed1b8ea423bc6170'
ad_account_id = 'act_635518447704085'
audience_name = 'customer'
audience_retention_days = '30'
pixel_id = '468823584956114'
app_id = '353577789953765'
FacebookAdsApi.init(access_token=access_token,api_version='v13.0')

fields = [
]
params = {
    'name': 'My Campaign',
    'buying_type': 'AUCTION',
    'objective': 'LINK_CLICKS',
    'special_ad_categories':'NONE',
    'status': 'PAUSED',
}
# campaign = AdAccount(ad_account_id).create_campaign(
#     fields=fields,
#     params=params,
# )
# print ('campaign', campaign)

campaign_id = '120330000103750809' #campaign.get_id()
print ('campaign_id:', campaign_id, '\n')

fields = [
]
params = {
  'name': 'My new Custom Audience',
  'subtype': 'CUSTOM',
  'description': 'People who purchased on my website',
  'customer_file_source': 'USER_PROVIDED_ONLY',
}
# params = {
#     'pixel_id': pixel_id,
#     'name': audience_name,
#     # 'subtype': 'WEBSITE',
#     'retention_days': audience_retention_days,
#     'rule': {'url':{'i_contains':''}},
#     'prefill': True,
# }
custom_audience = AdAccount(ad_account_id).create_custom_audience(
    fields=fields,
    params=params,
)
print ('custom_audience', custom_audience)

custom_audience_id = custom_audience.get_id()
print ('custom_audience_id:', custom_audience_id, '\n')

# fields = [
# ]
# params = {
#     'name': 'My AdSet',
#     'optimization_goal': 'REACH',
#     'billing_event': 'IMPRESSIONS',
#     'bid_amount': '20',
#     'daily_budget': '1000',
#     'campaign_id': campaign_id,
#     'targeting': {'custom_audiences':[{'id':custom_audience_id}], 'geo_locations':{'countries':['US']}},
#     'status': 'PAUSED',
# }
# ad_set = AdAccount(ad_account_id).create_ad_set(
#     fields=fields,
#     params=params,
# )
# print ('ad_set', ad_set)

# ad_set_id = ad_set.get_id()
# print ('ad_set_id:', ad_set_id, '\n')

# fields = [
# ]
# params = {
#     'name': 'My Creative',
#     'title': 'My Page Like Ad',
#     'body': 'Like My Page',
#     'object_url': 'www.facebook.com',
#     'link_url': 'www.facebook.com',
#     'image_url': 'http://www.facebookmarketingdevelopers.com/static/images/resource_1.jpg',
# }
# creative = AdAccount(ad_account_id).create_ad_creative(
#     fields=fields,
#     params=params,
# )
# print ('creative', creative)

# creative_id = creative.get_id()
# print ('creative_id:', creative_id, '\n')

# fields = [
# ]
# params = {
#     'name': 'My Ad',
#     'adset_id': ad_set_id,
#     'creative': {'creative_id':creative_id},
#     'status': 'PAUSED',
# }
# ad = AdAccount(ad_account_id).create_ad(
#     fields=fields,
#     params=params,
# )
# print ('ad', ad)

# ad_id = ad.get_id()
# print ('ad_id:', ad_id, '\n')

# fields = [
# ]
# params = {
#     'ad_format': 'DESKTOP_FEED_STANDARD',
# }
# print (Ad(ad_id).get_previews(
#     fields=fields,
#     params=params,
# ))


