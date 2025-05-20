import {
	ScrollView,
	Image,
	Text,
	View,
	StyleSheet,
	Dimensions,
} from "react-native";
import { NativeStackScreenProps } from "@react-navigation/native-stack";
import { RootStackParamList } from "../navigation/AppNavigator";
import cardsData from "../../data/data.json";

type Props = NativeStackScreenProps<RootStackParamList, "CardDetail">;

const CardDetailScreen = ({ route }: Props) => {
	const { cardId } = route.params;
	const card = cardsData[cardId as keyof typeof cardsData];

	return (
		<ScrollView style={styles.container}>
			<Image
				source={{ uri: card.image }}
				style={styles.mainImage}
				resizeMode="cover"
			/>
			<View style={styles.content}>
				<Text style={styles.title}>{card.title}</Text>
				<Text style={styles.description}>{card.description}</Text>

				{card.any_image?.map((img, index) => (
					<Image
						key={index}
						source={{ uri: img }}
						style={styles.additionalImage}
						resizeMode="cover"
					/>
				))}
			</View>
		</ScrollView>
	);
};

const { width } = Dimensions.get("window");

const styles = StyleSheet.create({
	container: {
		flex: 1,
		backgroundColor: "#fff",
	},
	mainImage: {
		width: "100%",
		height: width * 0.8,
	},
	content: {
		padding: 20,
	},
	title: {
		fontSize: 24,
		fontWeight: "bold",
		marginBottom: 16,
	},
	description: {
		fontSize: 16,
		lineHeight: 24,
		marginBottom: 20,
	},
	additionalImage: {
		width: "100%",
		height: width * 0.6,
		marginBottom: 20,
		borderRadius: 8,
	},
});

export default CardDetailScreen;
