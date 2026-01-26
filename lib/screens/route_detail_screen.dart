import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:url_launcher/url_launcher.dart';

import '../models/city_model.dart';
import '../services/directions_service.dart';
import '../utils/map_theme.dart';
import 'detail_screen.dart';
import 'package:shared_preferences/shared_preferences.dart';
import '../l10n/app_localizations.dart';

class RouteDetailScreen extends StatefulWidget {
  final List<Highlight> places;
  final String? routeId; // Static route support

  const RouteDetailScreen({super.key, required this.places, this.routeId});

  @override
  State<RouteDetailScreen> createState() => _RouteDetailScreenState();
}

class _RouteDetailScreenState extends State<RouteDetailScreen> {
  // ... (mevcut kodlar)

// ...

    final result = await service.getDirections(
      origin: origin,
      destination: destination,
      waypoints: waypoints,
      routeId: widget.routeId, // Pass routeId
    );

    if (result != null && mounted) {
      setState(() {
        _infoDistance = result['distance_text'];
        _infoDuration = result['duration_text'];

        _polylines.add(
          Polyline(
            polylineId: const PolylineId("google_route"),
            points: result['polyline_points'],
            color: accent, // Teal -> Accent
            width: 5,
            jointType: JointType.round,
          ),
        );

        _isLoadingRoute = false;
      });

      _fitMapToBounds(result['bounds']);
    } else {
      if (mounted) setState(() => _isLoadingRoute = false);
    }
  }

  void _fitMapToBounds(Map<String, dynamic> boundsData) {
    if (_mapController == null) return;

    final ne = boundsData['northeast'];
    final sw = boundsData['southwest'];

    LatLngBounds bounds = LatLngBounds(
      southwest: LatLng(sw['lat'], sw['lng']),
      northeast: LatLng(ne['lat'], ne['lng']),
    );

    Future.delayed(const Duration(milliseconds: 300), () {
      _mapController!.animateCamera(CameraUpdate.newLatLngBounds(bounds, 60));
    });
  }

  // ------------------------------------------------------------------------------------
  // ★★★ TÜM TURU GOOGLE MAPS’TE BAŞLATAN FONKSİYON ★★★
  // ------------------------------------------------------------------------------------
  Future<void> _startFullRouteNavigation() async {
    if (routeList.isEmpty) return;

    // SharedPreferences'ten seçili şehir adını al (ör: "barcelona")
    final prefs = await SharedPreferences.getInstance();
    final cityName = prefs.getString("selectedCity") ?? "";

    String _buildSearchQuery(Highlight h) {
      final buffer = StringBuffer(h.name);

      if (h.area.isNotEmpty) {
        buffer.write(", ${h.area}");
      }
      if (cityName.isNotEmpty) {
        buffer.write(", $cityName");
      }

      return Uri.encodeComponent(buffer.toString());
    }

    // Origin & Destination
    final origin = _buildSearchQuery(routeList.first);
    final destination = _buildSearchQuery(routeList.last);

    // Waypoints
    List<String> waypointList = [];
    if (routeList.length > 2) {
      for (int i = 1; i < routeList.length - 1; i++) {
        waypointList.add(_buildSearchQuery(routeList[i]));
      }
    }

    final waypoints = waypointList.isNotEmpty
        ? "&waypoints=${waypointList.join('|')}"
        : "";

    final Uri url = Uri.parse(
      "https://www.google.com/maps/dir/?api=1"
      "&origin=$origin"
      "&destination=$destination"
      "$waypoints"
      "&travelmode=walking",
    );

    // iOS 26+'da canLaunchUrl bazen false dönebiliyor, direkt deneyelim
    try {
      await launchUrl(url, mode: LaunchMode.externalApplication);
    } catch (e) {
      // Hata durumunda sessizce geç
      debugPrint('Google Maps açılamadı: $e');
    }
  }

  // ------------------------------------------------------------------------------------
  // UI
  // ------------------------------------------------------------------------------------
  @override
  Widget build(BuildContext context) {
    if (routeList.isEmpty) {
      return Scaffold(
        appBar: AppBar(title: Text(AppLocalizations.instance.routeDetail)),
        body: Center(child: Text(AppLocalizations.instance.noPlaceSelected)),
      );
    }

    return Scaffold(
      backgroundColor: const Color(0xFFF5F5F7),
      body: Stack(
        children: [
          CustomScrollView(
            slivers: [
              SliverAppBar(
                expandedHeight: 300,
                pinned: true,
                backgroundColor: Colors.white,
                elevation: 0,
                flexibleSpace: FlexibleSpaceBar(
                  background: Stack(
                    children: [
                      GoogleMap(
                        initialCameraPosition: CameraPosition(
                          target: LatLng(
                            routeList.first.lat,
                            routeList.first.lng,
                          ),
                          zoom: 13,
                        ),
                        markers: _markers,
                        polylines: _polylines,
                        mapType: MapType.normal,
                        zoomControlsEnabled: false,
                        myLocationButtonEnabled: false,
                        onMapCreated: (c) {
                          _mapController = c;
                          if (_darkMapStyle != null) {
                            c.setMapStyle(_darkMapStyle);
                          }
                        },
                      ),
                      Positioned(
                        top: 0,
                        left: 0,
                        right: 0,
                        height: 100,
                        child: Container(
                          decoration: BoxDecoration(
                            gradient: LinearGradient(
                              begin: Alignment.topCenter,
                              end: Alignment.bottomCenter,
                              colors: [
                                Colors.black.withOpacity(0.3),
                                Colors.transparent,
                              ],
                            ),
                          ),
                        ),
                      ),
                      Positioned(
                        bottom: 16,
                        left: 16,
                        right: 16,
                        child: _buildInfoCard(),
                      ),
                    ],
                  ),
                ),
                leading: Container(
                  margin: const EdgeInsets.all(8),
                  decoration: const BoxDecoration(
                    color: Colors.white,
                    shape: BoxShape.circle,
                  ),
                  child: IconButton(
                    icon: const Icon(Icons.arrow_back, color: Colors.black),
                    onPressed: () => Navigator.pop(context),
                  ),
                ),
                title: Text(
                  AppLocalizations.instance.routePlan,
                  style: TextStyle(
                    color: Colors.black,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                centerTitle: true,
              ),

              SliverPadding(
                padding: const EdgeInsets.symmetric(
                  horizontal: 20,
                  vertical: 24,
                ),
                sliver: SliverList(
                  delegate: SliverChildBuilderDelegate(
                    (context, index) =>
                        _buildPremiumTimelineItem(routeList[index], index),
                    childCount: routeList.length,
                  ),
                ),
              ),

              const SliverToBoxAdapter(child: SizedBox(height: 100)),
            ],
          ),

          // ★★★ Alt kısım sabit AppLocalizations.instance.startRoute butonu ★★★
          Positioned(
            bottom: 20,
            left: 20,
            right: 20,
            child: GestureDetector(
              onTap: _startFullRouteNavigation,
              child: Container(
                padding: const EdgeInsets.symmetric(vertical: 18),
                decoration: BoxDecoration(
                  color: const WanderlustColors.accent,
                  borderRadius: BorderRadius.circular(18),
                  boxShadow: [
                    BoxShadow(
                      color: Colors.black.withOpacity(0.12),
                      blurRadius: 12,
                      offset: const Offset(0, 4),
                    ),
                  ],
                ),
                child: Center(
                  child: Text(
                    AppLocalizations.instance.startRoute,
                    style: TextStyle(
                      color: Colors.white,
                      fontWeight: FontWeight.w700,
                      fontSize: 17,
                    ),
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildInfoCard() {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 16),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(20),
        boxShadow: [
          BoxShadow(
            color: Colors.black.withOpacity(0.08),
            blurRadius: 15,
            offset: const Offset(0, 5),
          ),
        ],
      ),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceAround,
        children: [
          _stat(Icons.timer_outlined, _infoDuration, AppLocalizations.instance.duration),
          Container(height: 24, width: 1, color: Colors.grey.shade200),
          _stat(Icons.directions_walk, _infoDistance, AppLocalizations.instance.distance),
          Container(height: 24, width: 1, color: Colors.grey.shade200),
          _stat(Icons.place_outlined, "${routeList.length}", AppLocalizations.instance.stop),
        ],
      ),
    );
  }

  Widget _stat(IconData icon, String val, String label) {
    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        Row(
          children: [
            Icon(icon, size: 18, color: const WanderlustColors.accent),
            const SizedBox(width: 6),
            Text(
              val,
              style: const TextStyle(
                fontWeight: FontWeight.w700,
                fontSize: 15,
                color: Colors.black87,
              ),
            ),
          ],
        ),
        const SizedBox(height: 2),
        Text(
          label,
          style: TextStyle(
            color: Colors.grey.shade500,
            fontSize: 11,
            fontWeight: FontWeight.w500,
          ),
        ),
      ],
    );
  }

  Widget _buildPremiumTimelineItem(Highlight place, int index) {
    final hasImage = place.imageUrl != null && place.imageUrl!.isNotEmpty;

    return Padding(
      padding: const EdgeInsets.only(bottom: 24),
      child: GestureDetector(
        onTap: () {
          Navigator.push(
            context,
            MaterialPageRoute(builder: (_) => DetailScreen(place: place)),
          );
        },
        child: Container(
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(24),
            boxShadow: [
              BoxShadow(
                color: Colors.black.withOpacity(0.06),
                blurRadius: 15,
                offset: const Offset(0, 8),
              ),
            ],
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Stack(
                children: [
                  ClipRRect(
                    borderRadius: const BorderRadius.vertical(
                      top: Radius.circular(24),
                    ),
                    child: hasImage
                        ? Image.network(
                            place.imageUrl!,
                            height: 180,
                            width: double.infinity,
                            fit: BoxFit.cover,
                          )
                        : Container(height: 180, color: Colors.grey.shade200),
                  ),

                  Positioned(
                    top: 12,
                    left: 12,
                    child: Container(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 12,
                        vertical: 8,
                      ),
                      decoration: BoxDecoration(
                        color: Colors.black.withOpacity(0.75),
                        borderRadius: BorderRadius.circular(12),
                      ),
                      child: Text(
                        AppLocalizations.instance.stopNumber(index + 1),
                        style: const TextStyle(
                          color: Colors.white,
                          fontWeight: FontWeight.bold,
                          fontSize: 12,
                        ),
                      ),
                    ),
                  ),

                  Positioned(
                    top: 12,
                    right: 12,
                    child: Container(
                      padding: const EdgeInsets.symmetric(
                        horizontal: 10,
                        vertical: 6,
                      ),
                      decoration: BoxDecoration(
                        color: Colors.white,
                        borderRadius: BorderRadius.circular(20),
                      ),
                      child: Text(
                        AppLocalizations.instance.translateCategory(place.category).toUpperCase(),
                        style: const TextStyle(
                          fontSize: 10,
                          fontWeight: FontWeight.w900,
                          color: Colors.black87,
                        ),
                      ),
                    ),
                  ),
                ],
              ),

              Padding(
                padding: const EdgeInsets.all(18),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      place.getLocalizedName(AppLocalizations.instance.isEnglish),
                      style: const TextStyle(
                        fontSize: 20,
                        fontWeight: FontWeight.w800,
                        color: Colors.black87,
                      ),
                    ),
                    const SizedBox(height: 6),
                    Text(
                      place.area.isNotEmpty ? place.area : (place.city ?? ""),
                      style: TextStyle(
                        color: Colors.grey.shade500,
                        fontSize: 14,
                        fontWeight: FontWeight.w500,
                      ),
                    ),
                    const SizedBox(height: 16),
                    Wrap(
                      spacing: 8,
                      children: place.tags.take(3).map((tag) {
                        return Container(
                          padding: const EdgeInsets.symmetric(
                            horizontal: 10,
                            vertical: 5,
                          ),
                          decoration: BoxDecoration(
                            color: const WanderlustColors.accent.withOpacity(0.1),
                            borderRadius: BorderRadius.circular(8),
                          ),
                          child: Text(
                            "#${AppLocalizations.instance.translateCategory(tag)}",
                            style: TextStyle(
                              color: const WanderlustColors.accent.withOpacity(0.9),
                              fontSize: 12,
                              fontWeight: FontWeight.w600,
                            ),
                          ),
                        );
                      }).toList(),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
