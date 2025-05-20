import { createNativeStackNavigator } from "@react-navigation/native-stack";
import HomeScreen from "../pages/HomeScreen";
import CardDetailScreen from "../pages/CardDetailScreen";

export type RootStackParamList = {
	Home: undefined;
	CardDetail: { cardId: string };
};

const Stack = createNativeStackNavigator<RootStackParamList>();

const AppNavigator = () => {
	return (
		<Stack.Navigator initialRouteName="Home">
			<Stack.Screen
				name="Home"
				component={HomeScreen}
				options={{ title: "Каталог товаров" }}
			/>
			<Stack.Screen
				name="CardDetail"
				component={CardDetailScreen}
				options={{ title: "Детали товара" }}
			/>
		</Stack.Navigator>
	);
};

export default AppNavigator;
