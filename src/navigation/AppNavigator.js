import { createStackNavigator } from '@react-navigation/stack';
import ProductsList from '../components/CardList';
import ProductDetailScreen from '../pages/HomePage';

const Stack = createStackNavigator();

const AppNavigator = () => {
    return (
        <Stack.Navigator initialRouteName="Products">
            <Stack.Screen
                name="Products"
                component={ProductsListScreen}
                options={{ title: 'Карточки личностей' }}
            />
            <Stack.Screen
                name="ProductDetail"
                component={ProductDetailScreen}
                options={({ route }) => ({ title: route.params.product.title })}
            />
        </Stack.Navigator>
    );
};

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

export default AppNavigator;
