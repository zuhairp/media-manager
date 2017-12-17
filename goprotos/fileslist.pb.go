// Code generated by protoc-gen-go. DO NOT EDIT.
// source: fileslist.proto

package media_manager

import proto "github.com/golang/protobuf/proto"
import fmt "fmt"
import math "math"

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

type FilesListRequest struct {
	Location Location `protobuf:"varint,1,opt,name=location,enum=media_manager.Location" json:"location,omitempty"`
}

func (m *FilesListRequest) Reset()                    { *m = FilesListRequest{} }
func (m *FilesListRequest) String() string            { return proto.CompactTextString(m) }
func (*FilesListRequest) ProtoMessage()               {}
func (*FilesListRequest) Descriptor() ([]byte, []int) { return fileDescriptor1, []int{0} }

func (m *FilesListRequest) GetLocation() Location {
	if m != nil {
		return m.Location
	}
	return Location_UNKNOWN
}

type FilesListResponse struct {
	Location  Location `protobuf:"varint,1,opt,name=location,enum=media_manager.Location" json:"location,omitempty"`
	Filenames []string `protobuf:"bytes,2,rep,name=filenames" json:"filenames,omitempty"`
}

func (m *FilesListResponse) Reset()                    { *m = FilesListResponse{} }
func (m *FilesListResponse) String() string            { return proto.CompactTextString(m) }
func (*FilesListResponse) ProtoMessage()               {}
func (*FilesListResponse) Descriptor() ([]byte, []int) { return fileDescriptor1, []int{1} }

func (m *FilesListResponse) GetLocation() Location {
	if m != nil {
		return m.Location
	}
	return Location_UNKNOWN
}

func (m *FilesListResponse) GetFilenames() []string {
	if m != nil {
		return m.Filenames
	}
	return nil
}

func init() {
	proto.RegisterType((*FilesListRequest)(nil), "media_manager.FilesListRequest")
	proto.RegisterType((*FilesListResponse)(nil), "media_manager.FilesListResponse")
}

func init() { proto.RegisterFile("fileslist.proto", fileDescriptor1) }

var fileDescriptor1 = []byte{
	// 153 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0xe2, 0xe2, 0x4f, 0xcb, 0xcc, 0x49,
	0x2d, 0xce, 0xc9, 0x2c, 0x2e, 0xd1, 0x2b, 0x28, 0xca, 0x2f, 0xc9, 0x17, 0xe2, 0xcd, 0x4d, 0x4d,
	0xc9, 0x4c, 0x8c, 0xcf, 0x4d, 0xcc, 0x4b, 0x4c, 0x4f, 0x2d, 0x92, 0xe2, 0x4e, 0xcd, 0x2b, 0xcd,
	0x2d, 0x86, 0xc8, 0x29, 0xb9, 0x73, 0x09, 0xb8, 0x81, 0x94, 0xfb, 0x64, 0x16, 0x97, 0x04, 0xa5,
	0x16, 0x96, 0xa6, 0x16, 0x97, 0x08, 0x19, 0x73, 0x71, 0xe4, 0xe4, 0x27, 0x27, 0x96, 0x64, 0xe6,
	0xe7, 0x49, 0x30, 0x2a, 0x30, 0x6a, 0xf0, 0x19, 0x89, 0xeb, 0xa1, 0x18, 0xa1, 0xe7, 0x03, 0x95,
	0x0e, 0x82, 0x2b, 0x54, 0x4a, 0xe3, 0x12, 0x44, 0x32, 0xa8, 0xb8, 0x20, 0x3f, 0xaf, 0x38, 0x95,
	0x2c, 0x93, 0x84, 0x64, 0xb8, 0x38, 0x41, 0x3e, 0xc8, 0x4b, 0xcc, 0x4d, 0x2d, 0x96, 0x60, 0x52,
	0x60, 0xd6, 0xe0, 0x0c, 0x42, 0x08, 0x24, 0xb1, 0x81, 0xdd, 0x6d, 0x0c, 0x08, 0x00, 0x00, 0xff,
	0xff, 0x14, 0x61, 0x2e, 0x3d, 0xe6, 0x00, 0x00, 0x00,
}
