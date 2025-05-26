import {
    View,
    ScrollView,
    Image,
    Text,
    StyleSheet,
    Dimensions,
    TouchableOpacity,
} from 'react-native';
import { useState } from 'react';

const ProductDetailScreen = ({ route }) => {
    const { product } = route.params;
    const { width, height } = Dimensions.get('window');
    const [mainImage, setMainImage] = useState(product.mainImage);

    // Размеры изображений (адаптивные)
    const mainImageHeight = height * 0.35;
    const thumbnailSize = width * 0.18;

    return (
        <ScrollView
            style={styles.container}
            contentContainerStyle={styles.scrollContent}
            scrollEnabled={true}
        >
            {/* Основное фото */}
            <Text style={styles.sectionTitle}>Основная информация</Text>
            <View style={styles.main_info}>
                <View
                    style={[
                        styles.mainImageContainer,
                        { height: mainImageHeight },
                    ]}
                >
                    <Image
                        source={{ uri: mainImage }}
                        style={styles.mainImage}
                        resizeMode="contain"
                    />
                </View>
                <Text>{product.shortDescription}</Text>
            </View>

            {/* Дополнительная информация */}
            <View>
                <Text>
                    {product.longDescription}
                </Text>
            </View>

            {/* Отдельно про память */}
            <View></View>

            {/* Дополнительные фото */}
            {product.additionalImages.length > 0 && (
                <>
                    <Text style={styles.sectionTitle}>Дополнительные фото</Text>
                    <ScrollView
                        horizontal
                        showsHorizontalScrollIndicator={false}
                        style={styles.thumbnailsContainer}
                    >
                        <View style={styles.thumbnailsRow}>
                            <TouchableOpacity
                                onPress={() => setMainImage(product.mainImage)}
                                style={[
                                    styles.thumbnail,
                                    mainImage === product.mainImage &&
                                        styles.selectedThumbnail,
                                    {
                                        width: thumbnailSize,
                                        height: thumbnailSize,
                                    },
                                ]}
                            >
                                <Image
                                    source={{ uri: product.mainImage }}
                                    style={styles.thumbnailImage}
                                    resizeMode="cover"
                                />
                            </TouchableOpacity>

                            {product.additionalImages.map((image, index) => (
                                <TouchableOpacity
                                    key={index}
                                    onPress={() => setMainImage(image)}
                                    style={[
                                        styles.thumbnail,
                                        mainImage === image &&
                                            styles.selectedThumbnail,
                                        {
                                            width: thumbnailSize,
                                            height: thumbnailSize,
                                        },
                                    ]}
                                >
                                    <Image
                                        source={{ uri: image }}
                                        style={styles.thumbnailImage}
                                        resizeMode="cover"
                                    />
                                </TouchableOpacity>
                            ))}
                        </View>
                    </ScrollView>
                </>
            )}

            {/* Описание товара */}
            <View style={styles.detailsSection}>
                <Text style={styles.productTitle}>{product.title}</Text>
                <Text style={styles.productDescription}>
                    {product.longDescription}
                </Text>
            </View>
        </ScrollView>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
    },
    scrollContent: {
        padding: 15,
        paddingBottom: 30,
    },
    sectionTitle: {
        fontSize: 16,
        fontWeight: '600',
        color: '#333',
        marginBottom: 10,
        marginTop: 5,
    },
    main_info: {
        backgroundColor: '#F8F8F8',
        flexDirection: 'row',
    },
    mainImageContainer: {
        width: '30%',
        marginBottom: 15,
        alignItems: 'left',
        borderRadius: 2,
        // overflow: 'hidden',
    },
    mainImage: {
        width: '100%',
        height: '100%',
    },
    thumbnailsContainer: {
        marginBottom: 20,
    },
    thumbnailsRow: {
        flexDirection: 'row',
        gap: 10,
    },
    thumbnail: {
        borderRadius: 6,
        overflow: 'hidden',
        borderWidth: 1,
        borderColor: '#e0e0e0',
    },
    selectedThumbnail: {
        borderColor: '#007AFF',
        borderWidth: 2,
    },
    thumbnailImage: {
        width: '100%',
        height: '100%',
    },
    detailsSection: {
        marginTop: 10,
    },
    productTitle: {
        fontSize: 20,
        fontWeight: '700',
        color: '#333',
        marginBottom: 15,
    },
    productDescription: {
        fontSize: 15,
        lineHeight: 22,
        color: '#555',
    },
});

export default ProductDetailScreen;
