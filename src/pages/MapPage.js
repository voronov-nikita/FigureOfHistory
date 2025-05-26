import WebMap from '../components/TheMap';
import { View } from 'react-native-web';

const MapScreen = () => {
    const markers = [
        {
            id: 1,
            title: 'Историческое место',
            description: 'Важное событие произошло здесь в 1812 году',
            details: 'Подробное описание исторического события...',
            lat: 55.7558,
            lng: 37.6176,
            imageUrl: 'https://example.com/historical-place.jpg',
            iconUrl: 'https://cdn-icons-png.flaticon.com/512/447/447031.png',
        },
        {
            id: 2,
            title: 'Музей',
            description: 'Крупнейший музей города',
            lat: 55.752,
            lng: 37.6155,
            imageUrl: 'https://example.com/museum.jpg',
        },
    ];

    const handleMarkerPress = marker => {
        console.log('Выбрана метка:', marker.title);
    };

    return (
        <View style={{alignContent: 'center', alignItems: 'center'}}>
            <div style={{ height: '100vh', width: '80%' }}>
                <WebMap markers={markers} onMarkerPress={handleMarkerPress} />
            </div>
        </View>
    );
};

export default MapScreen;