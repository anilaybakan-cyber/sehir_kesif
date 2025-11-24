import 'package:flutter/material.dart';
import 'package:cached_network_image/cached_network_image.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:share_plus/share_plus.dart';

import '../models/city_model.dart';

class DetailScreen extends StatefulWidget {
  final Highlight place;

  const DetailScreen({super.key, required this.place});

  @override
  State<DetailScreen> createState() => _DetailScreenState();
}

class _DetailScreenState extends State<DetailScreen> {
  bool isFavorite = false;
  int currentPhotoIndex = 0;
  GoogleMapController? _mapController;

  late List<String> photoGallery;

  @override
  void initState() {
    super.initState();
    _loadFavoriteStatus();

    photoGallery = [
      widget.place.displayImage,
      'https://images.unsplash.com/photo-1583422409516-2895a77efded?w=800',
      'https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?w=800',
      'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800',
    ];
  }

  @override
  void dispose() {
    _mapController?.dispose();
    super.dispose();
  }

  // -----------------------------
  // FAVORİ YÜKLE
  // -----------------------------
  Future<void> _loadFavoriteStatus() async {
    final prefs = await SharedPreferences.getInstance();
    final favorites = prefs.getStringList('favorite_places') ?? [];

    setState(() {
      isFavorite = favorites.contains(widget.place.name);
    });
  }

  // -----------------------------
  // FAVORİ AÇ/KAPAT
  // -----------------------------
  Future<void> _toggleFavorite() async {
    final prefs = await SharedPreferences.getInstance();
    List<String> favorites = prefs.getStringList('favorite_places') ?? [];

    setState(() {
      if (isFavorite) {
        favorites.remove(widget.place.name);
      } else {
        favorites.add(widget.place.name);
      }
      isFavorite = !isFavorite;
    });

    await prefs.setStringList('favorite_places', favorites);
  }

  // -----------------------------
  // PAYLAŞ
  // -----------------------------
  void _sharePlace() {
    Share.share(
      '${widget.place.name}\n\n${widget.place.description}\n\n📍 ${widget.place.area}',
      subject: 'Harika bir yer buldum!',
    );
  }

  // -----------------------------
  // UI
  // -----------------------------
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      body: CustomScrollView(
        slivers: [
          SliverAppBar(
            expandedHeight: 400,
            pinned: true,
            backgroundColor: Colors.white,
            leading: _buildBackButton(),
            actions: [_buildShareButton(), _buildFavoriteButton()],
            flexibleSpace: FlexibleSpaceBar(background: _buildPhotoGallery()),
          ),

          SliverToBoxAdapter(
            child: Container(
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.vertical(top: Radius.circular(30)),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  SizedBox(height: 24),
                  _buildHeader(),
                  SizedBox(height: 24),
                  _buildLocationInfo(),
                  SizedBox(height: 24),
                  _buildDescription(),
                  SizedBox(height: 24),
                  _buildTags(),
                  SizedBox(height: 24),
                  _buildMap(),
                  SizedBox(height: 24),
                  _buildSimilarPlaces(),
                  SizedBox(height: 40),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }

  // -----------------------------
  // FOTOĞRAF GALERİSİ
  // -----------------------------
  Widget _buildPhotoGallery() {
    return Stack(
      children: [
        PageView.builder(
          itemCount: photoGallery.length,
          onPageChanged: (index) {
            setState(() => currentPhotoIndex = index);
          },
          itemBuilder: (context, index) {
            return CachedNetworkImage(
              imageUrl: photoGallery[index],
              fit: BoxFit.cover,
              placeholder: (context, url) => Container(
                color: Colors.grey.shade200,
                child: Center(
                  child: CircularProgressIndicator(color: Colors.teal),
                ),
              ),
            );
          },
        ),

        // Alt gradient
        Positioned(
          bottom: 0,
          left: 0,
          right: 0,
          child: Container(
            height: 150,
            decoration: BoxDecoration(
              gradient: LinearGradient(
                begin: Alignment.topCenter,
                end: Alignment.bottomCenter,
                colors: [Colors.transparent, Colors.black.withOpacity(0.7)],
              ),
            ),
          ),
        ),

        // Foto sayacı
        Positioned(
          bottom: 20,
          right: 20,
          child: Container(
            padding: EdgeInsets.symmetric(horizontal: 12, vertical: 6),
            decoration: BoxDecoration(
              color: Colors.black.withOpacity(0.6),
              borderRadius: BorderRadius.circular(20),
            ),
            child: Text(
              '${currentPhotoIndex + 1}/${photoGallery.length}',
              style: TextStyle(color: Colors.white, fontSize: 13),
            ),
          ),
        ),
      ],
    );
  }

  // -----------------------------
  // FAVORİ BUTONU (YENİ)
  // -----------------------------
  Widget _buildFavoriteButton() {
    return Container(
      margin: EdgeInsets.only(right: 8, top: 8, bottom: 8),
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.9),
        shape: BoxShape.circle,
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.1),
            blurRadius: 10,
            offset: Offset(0, 2),
          ),
        ],
      ),
      child: IconButton(
        icon: AnimatedSwitcher(
          duration: Duration(milliseconds: 300),
          transitionBuilder: (child, animation) {
            return ScaleTransition(scale: animation, child: child);
          },
          child: Icon(
            isFavorite ? Icons.favorite : Icons.favorite_border,
            key: ValueKey(isFavorite),
            color: isFavorite ? Colors.red : Colors.black87,
            size: 24,
          ),
        ),
        onPressed: _toggleFavorite,
      ),
    );
  }

  // -----------------------------
  // PAYLAŞ BUTONU
  // -----------------------------
  Widget _buildShareButton() {
    return Container(
      margin: EdgeInsets.all(8),
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.9),
        shape: BoxShape.circle,
      ),
      child: IconButton(
        icon: Icon(Icons.share_outlined, color: Colors.black87),
        onPressed: _sharePlace,
      ),
    );
  }

  // -----------------------------
  // BACK BUTTON
  // -----------------------------
  Widget _buildBackButton() {
    return Container(
      margin: EdgeInsets.all(8),
      decoration: BoxDecoration(
        color: Colors.white.withOpacity(0.9),
        shape: BoxShape.circle,
      ),
      child: IconButton(
        icon: Icon(Icons.arrow_back_ios_new, color: Colors.black87, size: 20),
        onPressed: () => Navigator.pop(context),
      ),
    );
  }

  // -----------------------------
  // BAŞLIK
  // -----------------------------
  Widget _buildHeader() {
    return Padding(
      padding: EdgeInsets.symmetric(horizontal: 24),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            widget.place.name,
            style: TextStyle(
              fontSize: 32,
              fontWeight: FontWeight.bold,
              color: Colors.black87,
              height: 1.2,
            ),
          ),
          SizedBox(height: 12),
        ],
      ),
    );
  }

  // -----------------------------
  // KONUM KARTI
  // -----------------------------
  Widget _buildLocationInfo() {
    return Padding(
      padding: EdgeInsets.symmetric(horizontal: 24),
      child: Container(
        padding: EdgeInsets.all(16),
        decoration: BoxDecoration(
          color: Colors.grey.shade50,
          borderRadius: BorderRadius.circular(16),
          border: Border.all(color: Colors.grey.shade200),
        ),
        child: Row(
          children: [
            Icon(Icons.location_on, color: Colors.teal, size: 30),
            SizedBox(width: 16),
            Expanded(
              child: Text(
                '${widget.place.area} • ${widget.place.distanceFromCenter.toStringAsFixed(1)} km',
                style: TextStyle(fontSize: 16),
              ),
            ),
          ],
        ),
      ),
    );
  }

  // -----------------------------
  // AÇIKLAMA
  // -----------------------------
  Widget _buildDescription() {
    return Padding(
      padding: EdgeInsets.symmetric(horizontal: 24),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            "Hakkında",
            style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
          ),
          SizedBox(height: 8),
          Text(
            widget.place.description,
            style: TextStyle(height: 1.6, color: Colors.grey.shade700),
          ),
        ],
      ),
    );
  }

  // -----------------------------
  // TAGLER
  // -----------------------------
  Widget _buildTags() {
    return Padding(
      padding: EdgeInsets.symmetric(horizontal: 24),
      child: Wrap(
        spacing: 8,
        runSpacing: 8,
        children: widget.place.tags.map((tag) {
          return Container(
            padding: EdgeInsets.symmetric(horizontal: 12, vertical: 6),
            decoration: BoxDecoration(
              color: Colors.teal.withOpacity(0.1),
              borderRadius: BorderRadius.circular(12),
            ),
            child: Text(tag, style: TextStyle(color: Colors.teal.shade700)),
          );
        }).toList(),
      ),
    );
  }

  // -----------------------------
  // HARİTA
  // -----------------------------
  Widget _buildMap() {
    return Padding(
      padding: EdgeInsets.symmetric(horizontal: 24),
      child: Container(
        height: 200,
        child: ClipRRect(
          borderRadius: BorderRadius.circular(20),
          child: GoogleMap(
            initialCameraPosition: CameraPosition(
              target: LatLng(widget.place.lat, widget.place.lng),
              zoom: 15,
            ),
            markers: {
              Marker(
                markerId: MarkerId(widget.place.name),
                position: LatLng(widget.place.lat, widget.place.lng),
              ),
            },
            zoomControlsEnabled: false,
            myLocationButtonEnabled: false,
            onMapCreated: (c) => _mapController = c,
          ),
        ),
      ),
    );
  }

  // -----------------------------
  // BENZER YERLER (mock)
  // -----------------------------
  Widget _buildSimilarPlaces() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Padding(
          padding: EdgeInsets.symmetric(horizontal: 24),
          child: Text(
            "Benzer Yerler",
            style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
          ),
        ),
        SizedBox(height: 12),
        SizedBox(
          height: 140,
          child: ListView.builder(
            scrollDirection: Axis.horizontal,
            padding: EdgeInsets.symmetric(horizontal: 24),
            itemCount: 5,
            itemBuilder: (context, index) {
              return Container(
                width: 120,
                margin: EdgeInsets.only(right: 12),
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(16),
                ),
                child: Column(
                  children: [
                    Container(
                      height: 80,
                      decoration: BoxDecoration(
                        borderRadius: BorderRadius.vertical(
                          top: Radius.circular(16),
                        ),
                        color: Colors.grey.shade200,
                      ),
                    ),
                    Padding(
                      padding: EdgeInsets.all(10),
                      child: Text("Yer ${index + 1}"),
                    ),
                  ],
                ),
              );
            },
          ),
        ),
      ],
    );
  }
}
