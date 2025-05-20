import { View, StyleSheet } from "react-native";
import CardGrid from "../modules/CardGrid";
import cardsData from "../../data/data.json";
import { NativeStackScreenProps } from "@react-navigation/native-stack";
import { RootStackParamList } from "../navigation/AppNavigator";

type Props = NativeStackScreenProps<RootStackParamList, "Home">;

const HomeScreen = ({ navigation }: Props) => {
	return (
		<View style={styles.container}>
			<CardGrid
				data={cardsData}
				onCardPress={(id) => navigation.navigate("CardDetail", { cardId: id })}
			/>
		</View>
	);
};

const styles = StyleSheet.create({
	container: {
		flex: 1,
		backgroundColor: "#f5f5f5",
	},
});

export default HomeScreen;
