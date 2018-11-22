import easy_env
 
PAUSE = easy_env.get_int('PAUSE', 10)
CALC_TIME = easy_env.get_int('CALC_TIME', 15)
DONE_TIME = easy_env.get_int('DONE_TIME', 300)
VCPU_COUNT = easy_env.get_int('VCPU_COUNT', 2)
IMAGE_ID = easy_env.get_str('IMAGE_ID', 'ami-14fb1073')
INSTANCE_TYPE = easy_env.get_str('INSTANCE_TYPE', 't2.medium')
INSTANCE_TAG = easy_env.get_str('INSTANCE_TAG', 'ForBacktests')
MAX_INSTANCES = easy_env.get_int('MAX_INSTANCES', 0)
REGION_NAME = easy_env.get_str('REGION_NAME', 'eu-west-2')
# TODO: Добавить тип маркета инстанса 
INSTANCE_MARKET_TYPE = easy_env.get_str('INSTANCE_MARKET_TYPE', 'On-Demand')

# PAUSE = os.environ.get('PAUSE')
# CALC_TIME = os.environ.get('CALC_TIME')
# DONE_TIME = os.environ.get('DONE_TIME')
# VCPU_COUNT = os.environ.get('VCPU_COUNT')
# IMAGE_ID = os.environ.get('IMAGE_ID')
# INSTANCE_TYPE = os.environ.get('PAUSE')
