from math import ceil
def ProductPostPrice(product_weight_g,send_from=None,send_to=None):
    """
    محاسبه هزینه پستی محصول ورژن 1
    محسابه قیمت با ملاک ارسال برون استانی
    """
    product_weight_kg=product_weight_g/1000
    price=1
    if product_weight_kg <= 0.5:
        weight = 0.5
    else:
        weight = ceil(product_weight_kg)
    # --------------------------------------------------------------------
    # برون استانی: کرایه های پستی به ازای وزن
    pishtaz_price = {0.5: 9240, 1: 12320, 2: 15400, 3: 16500}
    sefareshi_price = {0.5: 5830, 1: 8008, 2: 3, 3000: 12760}
    # --------------------------------------------------------------------
    weight_price=0
    try:  # وزن عادی مطابق تعریفه ها
        weight_price=pishtaz_price[weight]
    except:  # به ازای هر کیلو بیشتر از 3 کیلو 1000 هزینه
        extra_weight=weight-3
        weight_price = pishtaz_price[3]+(1000*extra_weight)
    # --------------------------------------------------------------------
    # هزینه های ثابت پستی
    qeyre_standard=0.25 # در صورت وجود جریمه 25 درصد از کل هزینه می باشد.
    bime = 800  # تعهد غرامت اجباری
    shenase = 390  # شناسه الکترونیک
    agahi = 1820  # آگهی تحویل الکترونیک
    sms = 650  # سرویس پیام کوتاه
    tozii = 3250  # تعیین زمان توزیع
    maliyat = 0.09  # جمع تمام هزینه های بالا در 9 درصد

    # جمع تمام موارد بالا:
    final_price = (qeyre_standard * weight_price) + bime + shenase + agahi + sms + tozii + weight_price
    maliyat *= final_price
    final_post_price = final_price+maliyat

    if final_post_price > 10000 and final_post_price <100000 :
        rounded_cost = (int(str(final_post_price)[0:2]) * 1000)
    else:
        rounded_cost = final_post_price
    return int(rounded_cost)


def ProductBoxPrice(size):
    """
    محسابه هزینه جعبه ورژن 1

    """
    box_price={
                         # طول * عرض * ارتفاع
        'size1':2703.6,   # 10 * 10 * 15
        'size2':4174.7,   # 10 * 15 * 20
        'size3':6245.7,   # 15 * 20 * 20
        'size4':8861.7,   # 20 * 20 * 30
        'size5':16055.0,  # 20 * 25 * 30
        'size6':18453.7,  # 20 * 25 * 45
        'size7':22159.7,  # 25 * 30 * 40
        'size8':33495.7,  # 35 * 45 * 55
        'size9':43850.7,
        'other':None,
    }
    return box_price[size]

