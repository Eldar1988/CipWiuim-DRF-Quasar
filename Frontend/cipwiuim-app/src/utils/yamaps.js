export default function (region, points=[], zoom=7) {
  ymaps.ready(init);

  function init(){
    let myMap = new ymaps.Map("map", {
      center: region.coordinates.split(','),
      zoom: zoom
    });

    if (points && points.length > 0) {
      points.forEach(item => {
        let coordinates = []
        item.coordinates.split(',').forEach(item => coordinates.push(+item))
        let myPlacemark = new ymaps.Placemark(coordinates, {
          // Чтобы балун и хинт открывались на метке, необходимо задать ей определенные свойства.
          balloonContentHeader: item.title,
          balloonContentBody: `<button style="padding: 5px 10px"><a href='/activities/${region.slug}/${item.slug}'>Подробнее</a></button>`,
          hintContent: item.title,
          balloonContentFooter: item.type.join(' ')
        });
        myMap.geoObjects.add(myPlacemark);
      })
    }

  }
}


