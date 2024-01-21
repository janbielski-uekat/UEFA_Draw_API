<h1>UEFA Draw API</h1>
<h2>Projekt zaliczeniowy z przedmiotu zaawansowane programowanie</h2>
<h4>Robert Baron, Jan Bielski</h4>
<h3>Opis projektu</h3>
Projekt stanowi API, które mogłoby być podstawą działania systemu wykorzystywanego przez UEFA w losowaniu par w fazie pucharowej ligi mistrzów.
Jego kluczowe funkcjonalności to:
<ol>
  <li>Przesyłanie, pobieranie i usuwanie listy drużyn zakwalifikowanych do fazy pucharowej.</li>
  <li>Zwracanie listy drużyn, które mogą zostać sparowane ze wskazaną drużyną.</li>
  <li>Przesyłanie informacji o dopbraniu wskazanych drużyn w parę</li>
</ol>
<h3>Specyfikacja techniczna</h3>
Projekt został zrealizowany w języku Python z wykorzystaniem biblioteki FastAPI. Rolę bazy danych pełni w nim cluster MongoDB. Został skonteneryzowany w technologii Docker oraz uprodukcyjniony na platformie Azure WebServices pod adresem: https://uefadrawapi.azurewebsites.net<br><br>
Ze względu na oszczędność zasobów aplikacja nie jest dostępna cały czas i zostanie zaprezentowana podczas zajęć.
