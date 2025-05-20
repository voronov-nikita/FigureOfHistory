import { FlatList, View, StyleSheet, Dimensions } from "react-native";
import Card from "./Card";

interface CardGridProps {
	data: Record<string, any>;
	onCardPress: (id: string) => void;
}

const CardGrid = ({ data, onCardPress }: CardGridProps) => {
	const cardsArray = Object.entries(data).map(([id, item]) => ({
		id,
		...item,
	}));
	const { width } = Dimensions.get("window");
	const numColumns = width < 600 ? (width < 400 ? 1 : 2) : 3;

	return (
		<View style={styles.container}>
			<FlatList
				data={cardsArray}
				keyExtractor={(item) => item.id}
				renderItem={({ item }) => (
					<Card item={item} onPress={() => onCardPress(item.id)} />
				)}
				numColumns={numColumns}
				contentContainerStyle={styles.list}
				columnWrapperStyle={numColumns > 1 ? styles.columnWrapper : undefined}
				key={numColumns}
			/>
		</View>
	);
};

const styles = StyleSheet.create({
	container: {
		flex: 1,
		padding: 8,
	},
	list: {
		paddingBottom: 20,
	},
	columnWrapper: {
		justifyContent: "space-between",
	},
});

export default CardGrid;
