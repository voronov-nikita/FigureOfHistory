import { TouchableOpacity } from 'react-native';
import { createDrawerNavigator } from '@react-navigation/drawer';
import { createStackNavigator } from '@react-navigation/stack';
import { DrawerActions } from '@react-navigation/native';
import Icon from 'react-native-vector-icons/MaterialIcons';
import ProductsList from '../components/CardList';
import ProductDetailScreen from '../pages/HomePage';
import MapScreen from '../pages/MapPage';
import { useNavigation } from '@react-navigation/native';


function ProductsListScreen({ navigation }) {
    const productsData = require('../../data/data.json').products;

    const handleProductPress = product => {
        navigation.navigate('ProductDetail', { product });
    };

    return (
        <ProductsList
            products={productsData}
            onProductPress={handleProductPress}
        />
    );
}

// 2. Создаем Stack Navigator
const Stack = createStackNavigator();

function ProductStack() {
    return (
        <Stack.Navigator
            screenOptions={({ navigation }) => ({
                headerStyle: {
                    backgroundColor: '#f8f8f8',
                    elevation: 0,
                    shadowOpacity: 0,
                },
                headerTintColor: '#000',
                headerTitleStyle: {
                    fontWeight: 'bold',
                },
                headerLeft: () => (
                    <TouchableOpacity
                        onPress={() =>
                            navigation.dispatch(DrawerActions.toggleDrawer())
                        }
                        style={{ marginLeft: 15 }}
                    >
                        <Icon name="menu" size={24} color="#000" />
                    </TouchableOpacity>
                ),
            })}
        >
            <Stack.Screen
                name="Products"
                component={ProductsListScreen}
                options={{ title: 'Список личностей' }}
            />
            <Stack.Screen
                name="ProductDetail"
                component={ProductDetailScreen}
                options={({ route }) => ({
                    title: route.params.product.title,
                    headerBackTitle: 'Назад',
                })}
            />
            <Stack.Screen
                name="Map"
                component={MapScreen}
                options={{
                    title: 'Карта памятных мест',
                    headerBackTitle: 'Назад',
                }}
            />
        </Stack.Navigator>
    );
}

// 3. Создаем Drawer Navigator
const Drawer = createDrawerNavigator();

export default function AppNavigator() {
    return (
        <Drawer.Navigator
            screenOptions={{
                headerShown: false,
                drawerStyle: {
                    backgroundColor: '#fff',
                    width: 240,
                },
            }}
        >
            <Drawer.Screen
                name="ProductStack"
                component={ProductStack}
                options={{ title: 'Главная' }}
            />
            {/* Дополнительные экраны Drawer */}
            <Drawer.Screen
                name="Map"
                component={MapScreen}
                options={{ title: 'Карта' }}
            />
        </Drawer.Navigator>
    );
}
