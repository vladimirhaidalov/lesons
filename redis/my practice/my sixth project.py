def calculate_bmi(weight,height):
    bmi = weight/(height**2)
    return bmi

underweight='Недостаточный вес'
normal_weight='Нормальный вес'
overweight='Избыточный вес'
obesity='Ожирение'

def interpret_bmi(bmi):
    if bmi<18.5:
        return underweight
    elif 18.5 <= bmi< 24.9:
        return normal_weight
    elif 25<=bmi<29.9:
        return overweight
    else:
        return obesity
def main():
    weight = float(input('Введите свой вес в килограммах: '))
    height = float(input('Введите свой рост в метрах: '))
    bmi = calculate_bmi( weight,height)
    interpretation = interpret_bmi(bmi)
    print("Ваш BMI: {:.2f}".format(bmi))
    print('Интерпретация: {}'.format(interpretation))

if __name__=="__main__":
    main() 


