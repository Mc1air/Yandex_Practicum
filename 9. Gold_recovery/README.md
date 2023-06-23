# Восстановление золота из руды

**Описание проекта:**
    
Данные находятся в трёх файлах:

    gold_industry_train.csv — обучающая выборка;
    gold_industry_test.csv — тестовая выборка;
    gold_industry_full.csv — исходные данные.

Данные индексируются датой и временем получения информации (признак date). Соседние по времени параметры часто похожи.
Некоторые параметры недоступны, потому что замеряются и/или рассчитываются значительно позже. Из-за этого в тестовой выборке отсутствуют некоторые признаки, которые могут быть в обучающей. Также в тестовом наборе нет целевых признаков.
Исходный датасет содержит обучающую и тестовую выборки со всеми признаками.
В нашем распоряжении сырые данные: их просто выгрузили из хранилища.

**Описание данных**
    
Технологический процесс

    Rougher feed — исходное сырье
    Rougher additions (или reagent additions) — флотационные реагенты: Xanthate, Sulphate, Depressant
      
        Xanthate — ксантогенат (промотер, или активатор флотации);
        Sulphate — сульфат (на данном производстве сульфид натрия);
        Depressant — депрессант (силикат натрия).
    Rougher process (англ. «грубый процесс») — флотация
    Rougher tails — отвальные хвосты
    Float banks — флотационная установка
    Cleaner process — очистка
    Rougher Au — черновой концентрат золота
    Final Au — финальный концентрат золота

Параметры этапов

    air amount — объём воздуха
    fluid levels — уровень жидкости
    feed size — размер гранул сырья
    feed rate — скорость подачи

**Цель исследования:** 
    
Подготовить прототип модели машинного обучения.    
Модель должна предсказать коэффициент восстановления золота из золотосодержащей руды.
Модель поможет оптимизировать производство, чтобы не запускать предприятие с убыточными характеристиками.

**Ход исследования:**
1. Подготовка данных
2. Анализ данных
3. Построение модели
4. Проверка модели