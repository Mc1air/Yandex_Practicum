# Выбор локации для скважины

**Описание проекта:**
    
Допустим, мы работаем в нефтедобывающей компании. Нужно решить, где бурить новую скважину.

Нам предоставлены пробы нефти в трёх регионах: в каждом 10 000 месторождений, где измерили качество нефти и объём её запасов.

Шаги для выбора локации:

- В избранном регионе ищут месторождения, для каждого определяют значения признаков;
- Строят модель и оценивают объём запасов;
- Выбирают месторождения с самым высокими оценками значений. Количество месторождений зависит от бюджета компании и стоимости разработки одной скважины;
- Прибыль равна суммарной прибыли отобранных месторождений.

**Цель исследования:**    
* Построить модель машинного обучения, которая поможет определить регион, где добыча принесёт наибольшую прибыль. Проанализировать возможную прибыль и риски.

**Инструменты и навыки:**
    
Python, Pandas, NumPy, Sklearn, SciPy, Bootstrap

**Вывод:**

1. Данные загружены и подготовлены к дальнейшей работе
2. Обучены и проверены модели
3. Подсчитаны средний запас сырья и RMSE модели
4. Рассчитан достаточный объём сырья для безубыточной разработки новой скважины
5. Рассчитана прибыль для скважин с максимальным оъёмом сырья
6. Подсчитаны: средняя прибыль, 95%-й доверительный интервал и риск убытков

По результатам исследования лучшим регионом для разработки скважин был выбран первый регион, т.к., по сравнению с двумя другими регионами, у первого наименьшее значение риска убытков и высокая средняя выручка.
