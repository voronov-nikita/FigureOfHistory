import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';

// Фикс для иконок маркеров
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
    iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
    iconUrl: require('leaflet/dist/images/marker-icon.png'),
    shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
});

const WebMap = ({ markers, onMarkerPress }) => {
    const neutralTileLayer =
        'https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png';


    return (
        <MapContainer
            center={[55.7558, 37.6176]}
            zoom={13}
            style={{ height: '100%', width: '100%' }}
        >
            <TileLayer
                url={neutralTileLayer}
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            />

            {markers.map(marker => {
                // Создаем кастомную иконку для маркера
                const customIcon = new L.Icon({
                    iconUrl:
                        marker.iconUrl ||
                        'https://cdn0.iconfinder.com/data/icons/small-n-flat/24/678111-map-marker-512.png',
                    iconSize: [32, 32],
                    iconAnchor: [16, 32],
                    popupAnchor: [0, -32],
                });

                return (
                    <Marker
                        key={marker.id}
                        position={[marker.lat, marker.lng]}
                        icon={customIcon}
                        eventHandlers={{
                            click: () => onMarkerPress(marker),
                        }}
                    >
                        <Popup>
                            <div style={{ maxWidth: '300px' }}>
                                <h3 style={{ marginTop: 0 }}>{marker.title}</h3>
                                {marker.imageUrl && (
                                    <img
                                        src={marker.imageUrl}
                                        alt={marker.title}
                                        style={{
                                            width: '100%',
                                            height: 'auto',
                                            marginBottom: '10px',
                                            borderRadius: '4px',
                                        }}
                                    />
                                )}
                                <p>{marker.description}</p>
                                {marker.details && (
                                    <p
                                        style={{
                                            fontStyle: 'italic',
                                            color: '#666',
                                        }}
                                    >
                                        {marker.details}
                                    </p>
                                )}
                            </div>
                        </Popup>
                    </Marker>
                );
            })}
        </MapContainer>
    );
};

export default WebMap;
