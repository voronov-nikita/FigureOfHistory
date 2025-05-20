import {
	TouchableOpacity,
	Image,
	Text,
	View,
	StyleSheet,
	Dimensions,
} from "react-native";

interface CardProps {
	item: {
		title: string;
		image: string;
		short_description: string;
	};
	onPress: () => void;
}

const Card = ({ item, onPress }: CardProps) => {
	const { width } = Dimensions.get("window");
	const cardWidth = (width - 40) / 2;

	return (
		<TouchableOpacity
			style={[styles.card, { width: cardWidth }]}
			onPress={onPress}
		>
			<Image
				source={{ uri: item.image }}
				style={styles.image}
				resizeMode="cover"
			/>
			<View style={styles.content}>
				<Text style={styles.title} numberOfLines={1}>
					{item.title}
				</Text>
				<Text style={styles.description} numberOfLines={2}>
					{item.short_description}
				</Text>
			</View>
		</TouchableOpacity>
	);
};

const styles = StyleSheet.create({
	card: {
		backgroundColor: "#fff",
		borderRadius: 12,
		margin: 8,
		shadowColor: "#000",
		shadowOffset: { width: 0, height: 2 },
		shadowOpacity: 0.1,
		shadowRadius: 6,
		elevation: 3,
		overflow: "hidden",
	},
	image: {
		width: "100%",
		aspectRatio: 1,
	},
	content: {
		padding: 12,
	},
	title: {
		fontSize: 16,
		fontWeight: "600",
		marginBottom: 4,
	},
	description: {
		fontSize: 14,
		color: "#666",
	},
});

export default Card;
