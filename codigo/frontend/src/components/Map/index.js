import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import mapStyle from './styles';  // Adjust the path according to your folder structure
import icon from "leaflet/dist/images/marker-icon.png";
import iconShadow from "leaflet/dist/images/marker-shadow.png";
import L from "leaflet";
export default function Map({ routes }) {
  const defaultPosition = [-22.9068, -43.1729]; // Latitude and longitude of Rio de Janeiro
  const defaultIcon = L.icon({ // Apply the standard icon to all marker instances.
    iconUrl: icon,
    shadowUrl: iconShadow,
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    tooltipAnchor: [16, -28],
  });
  
  L.Marker.prototype.options.icon = defaultIcon;

  return (
    <MapContainer center={defaultPosition} zoom={13} style={mapStyle}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"  // Usando OpenStreetMap como provedor de tiles
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />
      {routes.map((route, index) => (
        <Marker key={index} position={[route.latitude, route.longitude]}>
          <Popup>{route.description || 'Sem descrição'}</Popup>
        </Marker>
      ))}
    </MapContainer>
  );
}


