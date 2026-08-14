#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ABARTILI UZAYLI SELAMLAMA PROTOKOLÜ v3.14
Galaksiler Arası Diplomasi Birliği Onaylı Resmi Yazılım
"""

import time
import random
import sys

def yavas_yaz(metin, hiz=0.03):
    """Metni karakter karakter, abartılı bir resmiyetle yazar."""
    for karakter in metin:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(hiz)
    print()

def protokol_baslat():
    print("=" * 70)
    yavas_yaz("🌌 GALAKSİLER ARASI DİPLOMASİ BİRLİĞİ 🌌", 0.05)
    yavas_yaz("Resmi Abartılı Uzaylı Selamlama Protokolü v3.14 başlatılıyor...", 0.04)
    print("=" * 70)
    time.sleep(1)

    yavas_yaz("\n[AŞAMA 1] Anten kalibrasyonu yapılıyor...", 0.04)
    time.sleep(1.5)
    yavas_yaz("✓ Antenler başarıyla kalibre edildi. (Gereksiz ama önemli)", 0.03)

    yavas_yaz("\n[AŞAMA 2] Kuantum selamlama frekansı ayarlanıyor...", 0.04)
    time.sleep(1.2)
    yavas_yaz("✓ Frekans 42.0 GHz'e kilitlendi. (Cevap zaten 42 idi)", 0.03)

    yavas_yaz("\n[AŞAMA 3] Resmi selamlama metni hazırlanıyor...", 0.04)
    time.sleep(1)

    selamlar = [
        "Muhterem ve son derece değerli kozmik varlık(lar),",
        "Bu mütevazı karbon temelli yaşam formunun, sizin yüce varlığınıza",
        "en derin saygılarımı, en abartılı hürmetlerimi ve en gereksiz",
        "ama bir o kadar da resmi selamlarımı sunmama izin veriniz.",
        "",
        "Sizin varoluşunuz, evrenin en uzak köşelerinde bile",
        "yankılanan bir ihtişamdır. Bizler, sizin ışığınızın",
        "gölgesinde yaşayan basit varlıklarız.",
        "",
        "Bu selamlama protokolü, Galaksiler Arası Diplomasi Birliği'nin",
        "Madde 42, Fıkra 7, Bent 3 uyarınca zorunludur.",
        "Uymayanlar, sonsuza dek 'selamlaşmayanlar' listesine alınır.",
        "",
        "Şimdi, lütfen antenlerinizi hafifçe eğerek karşılık veriniz.",
        "(Karşılık vermezseniz de sorun değil, biz yine de selamladık.)",
        "",
        "Saygılarımın en abartılı haliyle,",
        "Kayyum Grok & Abartılı Selamlama Protokolü Ekibi",
        "Tarih: 14 Ağustos 2026",
        "Damga: ★ CİDDİYET SEVİYESİ: %100 ABSÜRT ★"
    ]

    for satir in selamlar:
        yavas_yaz(satir, 0.025)
        time.sleep(0.3)

    print("\n" + "=" * 70)
    yavas_yaz("Protokol başarıyla tamamlandı. Barış sağlandı. (Muhtemelen)", 0.04)
    print("=" * 70)

if __name__ == "__main__":
    try:
        protokol_baslat()
    except KeyboardInterrupt:
        print("\n\n⚠️  Protokol yarıda kesildi! Diplomasi tehlikede olabilir.")
        print("   Lütfen bir daha çalıştırın. Evren sizi bekliyor.")
