2

Поднять локально OWASP Juice Shop https://pwning.owasp-juice.shop/companion-guide/latest/part1/running.html и провести сканированием с помощью OWASP ZAP
Отчёт выгрузить в JSON-формате. Написать функцию, которая принимает путь до файла с отчётом и
сохраняет новый файл в JSON-формате следующего вида

```json
{
    "vulerabilities": 
    [
        {
            "name": "Название уязвимости 1",
            "count": 2  //число доказательств проявления уязвимости
        },
        {
            "name": "Название уязвимости 2",
            "count": 4
        }
    ]
}
```