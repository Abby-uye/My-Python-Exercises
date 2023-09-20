class Logistics:
    def riders_pay(self, number_of_delivery):
        salary = 0
        amount_per_parcel_less_than_50 = 160
        amount_per_parcel_less_than_60 = 200
        amount_per_parcel_less_than_70 = 250
        amount_per_parcel_greater_than_70 = 500
        base_pay = 5000
        if number_of_delivery < 50:
            salary = amount_per_parcel_less_than_50 * number_of_delivery + base_pay
        elif 50 <= number_of_delivery <= 59:
            salary = amount_per_parcel_less_than_60 * number_of_delivery + base_pay
        elif 60 <= number_of_delivery <= 69:
            salary = amount_per_parcel_less_than_70 * number_of_delivery + base_pay
        elif number_of_delivery >= 70:
            salary = amount_per_parcel_greater_than_70 * number_of_delivery + base_pay
        return salary

