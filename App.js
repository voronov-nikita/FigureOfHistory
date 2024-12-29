//
// Основной файл разработки и запуска приложения
//

import { NavigationContainer } from "@react-navigation/native";
import { createStackNavigator } from "@react-navigation/stack";
import React from "react";

// импорт отдельных модулей - страниц
import { MaterialScreen } from "./src/pages/MaterialPage";
import { AboutScreen } from "./src/pages/AboutPage";
import { HomeScreen } from "./src/pages/HomePage";

// конфигуратор навигации
const Stack = createStackNavigator();

export default function App() {

	return (
		<NavigationContainer>
			<Stack.Navigator
				initialRouteName="Home"
				screenOptions={{
					headerStyle: {
						backgroundColor: "#ffffff",
					},
				}}
			>

				<Stack.Screen
					name="Home"
					component={HomeScreen}
					options={{
						headerShown: false,
					}}
				/>

        <Stack.Screen
					name="About"
					component={AboutScreen}
					options={{
						headerShown: false,
					}}
				/>

        <Stack.Screen
					name="Material"
					component={MaterialScreen}
					options={{
						headerShown: false,
					}}
				/>
			</Stack.Navigator>
		</NavigationContainer>
	);
}