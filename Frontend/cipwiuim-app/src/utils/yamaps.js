export default function () {
  ymaps.ready(init);

  function init(){
    let myMap = new ymaps.Map("map", {
      center: [48.684590, 67.728947],
      zoom: 6
    });
    let myPlacemark = new ymaps.Placemark([48.047036, 70.750961], {
      // Чтобы балун и хинт открывались на метке, необходимо задать ей определенные свойства.
      balloonContentHeader: "title",
      balloonContentBody: "Содержимое <em>балуна</em> метки",
      hintContent: "Хинт метки"
    });

    myMap.geoObjects.add(myPlacemark);
  }
}


